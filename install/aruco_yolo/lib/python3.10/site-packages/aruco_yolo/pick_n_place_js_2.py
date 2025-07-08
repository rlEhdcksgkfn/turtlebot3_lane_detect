import rclpy
from rclpy.node import Node
from aruco_msgs.msg import MarkerArray
from geometry_msgs.msg import Twist, Pose, PoseArray
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint
from std_msgs.msg import Header, Bool
from sensor_msgs.msg import JointState
from turtlebot_cosmo_interface.srv import MoveitControl
from aruco_yolo.moveit_client import TurtlebotArmClient
import time
from transitions import Machine

# ANSI 색상 코드 (로그용)
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

class ArucoMarkerListener(Node, ArucoStateMachine):
    def __init__(self):
        super().__init__('aruco_marker_listener')
        ArucoStateMachine.__init__(self)

        # 파라미터 및 변수 초기화
        self.markerid = self.declare_parameter('markerid', 1).get_parameter_value().integer_value
        self.target_marker_id = self.markerid
        self.initial_positions = self.declare_parameter('initial_positions', [0.0698, -0.2967, -0.4538, 1.8326]).get_parameter_value().double_array_value
        self.workspace_bounds = {'x': [-0.5, 0.5], 'y': [-0.5, 0.5], 'z': [0.0, 0.3]}

        self.aruco_marker_found = False
        self.armrun = False
        self.aruco_position = {'x': 0.0, 'y': 0.0, 'z': 0.0}
        self.finish_move = False
        self.get_joint = False
        self.task_completed = False

        # 구독자
        self.aruco_subscription = self.create_subscription(MarkerArray, '/camera/detected_markers', self.aruco_listener_callback, 10)
        self.joint_subscription = self.create_subscription(JointState, '/joint_states', self.joint_states_callback, 10)

        # 퍼블리셔
        self.cmd_vel_publisher = self.create_publisher(Twist, '/cmd_vel', 2)
        self.joint_pub = self.create_publisher(JointTrajectory, '/arm_controller/joint_trajectory', 10)

        # 자율주행 활성/비활성 제어 퍼블리셔
        self.autonomous_enable_pub = self.create_publisher(Bool, '/autonomous_enable', 1)
        self.autonomous_drive = True  # 자율주행 활성 상태 변수

        # Twist, Trajectory 초기화
        self.twist = Twist()
        self.trajectory_msg = JointTrajectory()
        self.trajectory_msg.header = Header()
        self.trajectory_msg.joint_names = ['joint1', 'joint2', 'joint3', 'joint4']
        self.point = JointTrajectoryPoint()
        self.point.velocities = [0.0] * 4
        self.point.accelerations = [0.0] * 4
        self.point.time_from_start.sec = 0
        self.point.time_from_start.nanosec = 500

        self.move_to_initial_position()

    def move_to_initial_position(self):
        self.get_logger().info(f"[{time.strftime('%H:%M:%S')}] Moving to initial position")
        self.point.positions = self.initial_positions
        self.trajectory_msg.points = [self.point]
        self.joint_pub.publish(self.trajectory_msg)
        rclpy.spin_once(self, timeout_sec=0.5)

    def joint_states_callback(self, msg):
        if not self.get_joint:
            return
        for i, name in enumerate(msg.name):
            position = msg.position[i] if i < len(msg.position) else None
            if name in self.trajectory_msg.joint_names:
                self.get_logger().info(f"[{time.strftime('%H:%M:%S')}] {name}: {position}")

    def aruco_listener_callback(self, msg):
        self.aruco_marker_found = False
        for marker in msg.markers:
            if marker.id == self.target_marker_id:
                self.aruco_marker_found = True
                self.aruco_position = {
                    'x': marker.pose.pose.position.x,
                    'y': marker.pose.pose.position.y,
                    'z': marker.pose.pose.position.z
                }

                self.get_logger().info(f"[{time.strftime('%H:%M:%S')}] ✅ ArUco marker {marker.id} detected. Current state: {self.state}")
                self.get_logger().info(f"[{time.strftime('%H:%M:%S')}] Marker ID: {marker.id}, Position: x={self.aruco_position['x']}, y={self.aruco_position['y']}, z={self.aruco_position['z']}")

                if self.state == 'START':
                    self.marker_detected()

                # 마커 발견 시 자율주행 정지 신호 보내기
                if self.autonomous_drive:
                    self.get_logger().info(f"[{time.strftime('%H:%M:%S')}] 자율주행 중지 요청")
                    self.autonomous_enable_pub.publish(Bool(data=False))
                    self.autonomous_drive = False
                    self.publish_cmd_vel(0.0)

                if marker.id == 1:
                    self.get_logger().info(f"[{time.strftime('%H:%M:%S')}] Marker 1 detected!")
                elif marker.id == 2:
                    self.get_logger().info(f"[{time.strftime('%H:%M:%S')}] Marker 2 detected!")
                break

        if not self.aruco_marker_found and not self.armrun:
            self.get_logger().warn(f"[{time.strftime('%H:%M:%S')}] No ArUco marker detected. Staying at initial position.")
            self.move_to_initial_position()

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
        self.move_to_initial_position()

        corrected_z = min(max(2.09 * self.aruco_position['z'] - 5.55, self.workspace_bounds['z'][0]), self.workspace_bounds['z'][1])
        self.get_logger().info(
            f"[{time.strftime('%H:%M:%S')}] Mission ArUco marker coordinates: x={self.aruco_position['x']}, y={self.aruco_position['y']}, corrected_z={corrected_z}")

        if not (self.workspace_bounds['x'][0] <= self.aruco_position['x'] <= self.workspace_bounds['x'][1] and
                self.workspace_bounds['y'][0] <= self.aruco_position['y'] <= self.workspace_bounds['y'][1] and
                self.workspace_bounds['z'][0] <= corrected_z <= self.workspace_bounds['z'][1]):
            self.get_logger().error(f"[{time.strftime('%H:%M:%S')}] ArUco marker position out of workspace bounds")
            self.armrun = False
            return

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
                    break
                else:
                    self.get_logger().warn(f"[{time.strftime('%H:%M:%S')}] Attempt {attempt+1} failed: {description}")
                    if attempt == max_retries - 1:
                        self.get_logger().error(f"[{time.strftime('%H:%M:%S')}] Failed after {max_retries} attempts: {description}")
                        self.armrun = False
                        return
                    time.sleep(1.0)
                rclpy.spin_once(self, timeout_sec=1.0)

        self.get_logger().info(f"[{time.strftime('%H:%M:%S')}] Moving to target position")
        pose_array = self.append_pose_init(self.aruco_position['x'], self.aruco_position['y'], corrected_z)
        response = arm_client.send_request(0, "", pose_array)
        if response.response:
            self.get_logger().info(f"[{time.strftime('%H:%M:%S')}] Successfully moved to target position")
        else:
            self.get_logger().error(f"[{time.strftime('%H:%M:%S')}] Failed to move to target position")
            self.armrun = False
            return

        self.finish_move = True
        self.task_done()
        self.get_logger().info(f"[{time.strftime('%H:%M:%S')}] Mission completed")

        # 동작 완료 후 자율주행 재개 신호 보내기
        self.autonomous_enable_pub.publish(Bool(data=True))
        self.armrun = False
        self.autonomous_drive = True

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
