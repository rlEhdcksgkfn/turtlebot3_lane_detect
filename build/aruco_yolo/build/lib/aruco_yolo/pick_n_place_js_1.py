import rclpy
from rclpy.node import Node
from aruco_msgs.msg import MarkerArray
from geometry_msgs.msg import Twist, Pose, PoseArray
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint
from std_msgs.msg import Header
from sensor_msgs.msg import JointState
from turtlebot_cosmo_interface.srv import MoveitControl
from aruco_yolo.moveit_client import TurtlebotArmClient
import time
from transitions import Machine

# ANSI 색상 코드
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
MAGENTA = "\033[95m"
CYAN = "\033[96m"
RESET = "\033[0m"

class ArucoStateMachine:
    states = ['START', 'MOVING_TO_MARKER', 'ARM_CONTROL', 'COMPLETED']
    transitions = [
        {'trigger': 'marker_detected', 'source': 'START', 'dest': 'MOVING_TO_MARKER'},
        {'trigger': 'close_to_marker', 'source': 'MOVING_TO_MARKER', 'dest': 'ARM_CONTROL'},
        {'trigger': 'task_done', 'source': 'ARM_CONTROL', 'dest': 'COMPLETED'}
    ]

    def __init__(self):
        self.machine = Machine(model=self, states=self.states, transitions=self.transitions, initial='START')
        self.marker_subscriber = self.create_subscription(
        MarkerArray, 'detected_markers', self.aruco_listener_callback, 10)
        
class ArucoMarkerListener(Node, ArucoStateMachine):
    def __init__(self):
        super().__init__('aruco_marker_listener')
        ArucoStateMachine.__init__(self)

        # 파라미터 설정
        self.markerid = self.declare_parameter('markerid', 0).get_parameter_value().integer_value
        self.target_marker_id = self.markerid
        self.initial_positions = self.declare_parameter('initial_positions', [0.0698, -0.2967, -0.4538, 1.8326]).get_parameter_value().double_array_value
        self.workspace_bounds = {
            'x': [-0.5, 0.5], 'y': [-0.5, 0.5], 'z': [0.0, 0.3]
        }

        # 구독자
        self.aruco_subscription = self.create_subscription(
            MarkerArray, 'detected_markers', self.aruco_listener_callback, 10)
        self.joint_subscription = self.create_subscription(
            JointState, '/joint_states', self.joint_states_callback, 10)

        # 퍼블리셔
        self.cmd_vel_publisher = self.create_publisher(Twist, '/cmd_vel', 2)
        self.joint_pub = self.create_publisher(JointTrajectory, '/arm_controller/joint_trajectory', 10)
        self.twist = Twist()
        self.trajectory_msg = JointTrajectory()
        self.trajectory_msg.header = Header()
        self.trajectory_msg.joint_names = ['joint1', 'joint2', 'joint3', 'joint4']
        self.point = JointTrajectoryPoint()
        self.point.velocities = [0.0] * 4
        self.point.accelerations = [0.0] * 4
        self.point.time_from_start.sec = 0
        self.point.time_from_start.nanosec = 500

        # 상태 변수
        self.aruco_marker_found = False
        self.task_completed = False
        self.armrun = False
        self.aruco_position = {'x': 0.0, 'y': 0.0, 'z': 0.0}
        self.finish_move = False
        self.get_joint = False

        # 초기 위치로 이동
        self.move_to_initial_position()

    def move_to_initial_position(self):
        self.get_logger().info(f"[{time.strftime('%H:%M:%S')}] Moving to initial position")
        self.point.positions = self.initial_positions
        self.trajectory_msg.points = [self.point]
        self.joint_pub.publish(self.trajectory_msg)
        print("11111111111111111111")

    def joint_states_callback(self, msg):
        if not self.get_joint:
            return
        for i, name in enumerate(msg.name):
            position = msg.position[i] if i < len(msg.position) else None
            if name in self.trajectory_msg.joint_names:
                self.get_logger().info(f"[{time.strftime('%H:%M:%S')}] {name}: {position}")

    def aruco_listener_callback(self, msg: MarkerArray):
        if not msg.markers:
            return  # 마커가 없으면 함수 종료

        marker = msg.markers[0]  # 항상 마커는 하나뿐

        if marker.id == 1:
            self.aruco_position = {
                'x': marker.pose.pose.position.x,
                'y': marker.pose.pose.position.y,
                'z': marker.pose.pose.position.z
            }

            self.marker_detected()
            self.publish_cmd_vel(0.0)  # 즉시 정지
            self.finish_move = True
            self.close_to_marker()

            if not self.armrun:
                self.aruco_arm_controll()


    def publish_cmd_vel(self, linear_x):
        self.twist.linear.x = linear_x
        self.twist.angular.z = 0.0
        self.cmd_vel_publisher.publish(self.twist)
        self.get_logger().info(f"[{time.strftime('%H:%M:%S')}] Publishing cmd_vel: linear.x={linear_x}")

    def append_pose_init(self, x, y, z):
        pose_array = PoseArray()
        pose_array.header.frame_id = "base_link"
        pose_array.header.stamp = self.get_clock().now().to_msg()
        pose = Pose()
        pose.position.x = x
        pose.position.y = y
        pose.position.z = z
        pose_array.poses.append(pose)
        self.get_logger().info(f"[{time.strftime('%H:%M:%S')}] Pose initialized - x: {x}, y: {y}, z: {z}")
        return pose_array

    def aruco_arm_controll(self):
        self.get_logger().info(f"[{time.strftime('%H:%M:%S')}] Starting arm control")
        self.armrun = True
        arm_client = TurtlebotArmClient()

        # 초기 위치로 이동
        self.move_to_initial_position()
        if not self.wait_for_motion_completion(arm_client):
            self.get_logger().error(f"[{time.strftime('%H:%M:%S')}] Failed to move to initial position")
            self.armrun = False
            return

        # 작업 공간 확인 (z 보정 제거)
        if not (self.workspace_bounds['x'][0] <= self.aruco_position['x'] <= self.workspace_bounds['x'][1] and
                self.workspace_bounds['y'][0] <= self.aruco_position['y'] <= self.workspace_bounds['y'][1] and
                self.workspace_bounds['z'][0] <= self.aruco_position['z'] <= self.workspace_bounds['z'][1]):
            self.get_logger().error(f"[{time.strftime('%H:%M:%S')}] ArUco marker position out of workspace bounds")
            self.armrun = False
            return

        # MoveIt 동작 시퀀스
        moveit_steps = [
            (1, "01_home", "Move to home position"),
            (2, "open", "Gripper open"),
            (1, "02_box_front", "Move to box front"),
            (1, "03_move_to_box", "Move to box"),
            (2, "close", "Gripper close"),
            (1, "04_move_up", "Move up"),
            (1, "05_conveyor_up", "Move to conveyor up"),
            (1, "06_conveyor_down", "Move to conveyor down"),
            (2, "open", "Gripper open"),
            (1, "07_conveyor_up", "Move to conveyor up"),
            (1, "08_home", "Return to home position")
        ]

        max_retries = 3
        for cmd, posename, description in moveit_steps:
            self.get_logger().info(f"[{time.strftime('%H:%M:%S')}] Executing: {description}")
            for attempt in range(max_retries):
                response = arm_client.send_request(cmd, posename)
                if response.response:
                    self.get_logger().info(f"[{time.strftime('%H:%M:%S')}] Success: {description}")
                    if not self.wait_for_motion_completion(arm_client):
                        self.get_logger().error(f"[{time.strftime('%H:%M:%S')}] Motion not completed: {description}")
                        self.armrun = False
                        return
                    break
                else:
                    self.get_logger().warn(f"[{time.strftime('%H:%M:%S')}] Attempt {attempt+1} failed: {description}")
                    if attempt == max_retries - 1:
                        self.get_logger().error(f"[{time.strftime('%H:%M:%S')}] Failed after {max_retries} attempts: {description}")
                        self.armrun = False
                        return
                    time.sleep(1.0)

        # ArUco 마커 위치로 이동 (z 보정 제거)
        self.get_logger().info(f"[{time.strftime('%H:%M:%S')}] Moving to target position")
        pose_array = self.append_pose_init(self.aruco_position['x'], self.aruco_position['y'], self.aruco_position['z'])
        response = arm_client.send_request(0, "", pose_array)
        if response.response:
            self.get_logger().info(f"[{time.strftime('%H:%M:%S')}] Successfully moved to target position")
            if not self.wait_for_motion_completion(arm_client):
                self.get_logger().error(f"[{time.strftime('%H:%M:%S')}] Motion to target position not completed")
                self.armrun = False
                return
        else:
            self.get_logger().error(f"[{time.strftime('%H:%M:%S')}] Failed to move to target position")
            self.armrun = False
            return

        self.finish_move = True
        self.task_done()
        self.get_logger().info(f"[{time.strftime('%H:%M:%S')}] Mission completed")
        self.armrun = False

    def wait_for_motion_completion(self, arm_client, timeout=5.0):
        start_time = time.time()
        while time.time() - start_time < timeout:
            if arm_client.is_motion_completed():  # TurtlebotArmClient에 구현 필요
                return True
            rclpy.spin_once(self, timeout_sec=0.1)
        self.get_logger().error(f"[{time.strftime('%H:%M:%S')}] Motion timeout")
        return False

def main(args=None):
    rclpy.init(args=args)
    node = ArucoMarkerListener()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.get_logger().info(f"[{time.strftime('%H:%M:%S')}] Shutting down node")
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()