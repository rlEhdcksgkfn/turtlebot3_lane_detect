import rclpy
from rclpy.node import Node
from aruco_msgs.msg import MarkerArray
from geometry_msgs.msg import Twist
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint
from std_msgs.msg import Header
from sensor_msgs.msg import JointState
from transitions import Machine
from aruco_yolo.arm_ik import ArmIKController  # 직접 작성한 역기구학 모듈 사용

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

        self.markerid = self.declare_parameter('markerid', 1).get_parameter_value().integer_value
        self.target_marker_id = self.markerid
        self.initial_positions = self.declare_parameter('initial_positions', [0.0, 0.0, 0.0, 0.0]).get_parameter_value().double_array_value
        self.workspace_bounds = {'x': [-0.5, 0.5], 'y': [-0.5, 0.5], 'z': [0.0, 0.3]}

        self.aruco_subscription = self.create_subscription(
            MarkerArray, '/camera/detected_markers', self.aruco_listener_callback, 10)
        self.joint_subscription = self.create_subscription(
            JointState, '/joint_states', self.joint_states_callback, 10)

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

        self.ik_controller = ArmIKController(self.joint_pub)

        self.aruco_marker_found = False
        self.task_completed = False
        self.armrun = False
        self.aruco_position = {'x': 0.0, 'y': 0.0, 'z': 0.0}
        self.finish_move = False
        self.get_joint = False

        # 그리퍼 상태 (True: 닫힘, False: 열림)
        self.gripper_closed = False

        # 로봇 회전 관련 변수
        self.rotation_speed = 0.3  # rad/s
        self.rotation_time_90deg = 3.14 / self.rotation_speed  # 90도 회전 시간 예측

        self.move_to_initial_position()

    def move_to_initial_position(self):
        self.get_logger().info("Moving to initial position")
        self.point.positions = self.initial_positions
        self.trajectory_msg.points = [self.point]
        self.joint_pub.publish(self.trajectory_msg)
        print("111111111")

        
    def joint_states_callback(self, msg):
        if not self.get_joint:
            return
        for i, name in enumerate(msg.name):
            if name in self.trajectory_msg.joint_names:
                position = msg.position[i]
                self.get_logger().info(f"{name}: {position}")

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

                self.get_logger().info(f"Marker {marker.id} detected at x={self.aruco_position['x']:.2f}, "
                                       f"y={self.aruco_position['y']:.2f}, z={self.aruco_position['z']:.2f}, State: {self.state}")

                if self.state == 'START':
                    self.marker_detected()

                if self.state == 'MOVING_TO_MARKER':
                    if self.aruco_position['z'] > 0.21:
                        self.publish_cmd_vel(0.10)
                    else:
                        self.publish_cmd_vel(0.0)
                        self.finish_move = True
                        self.close_to_marker()
                        if not self.armrun:
                            self.pick_and_place_sequence()
                break

        if not self.aruco_marker_found and not self.armrun:
            self.get_logger().warn("No marker detected. Returning to initial position.")
            self.move_to_initial_position()

    def publish_cmd_vel(self, linear_x=0.0, angular_z=0.0):
        self.twist.linear.x = linear_x
        self.twist.angular.z = angular_z
        self.cmd_vel_publisher.publish(self.twist)
        self.get_logger().info(f"cmd_vel: linear_x={linear_x}, angular_z={angular_z}")

    # 그리퍼 닫기 (잡기)
    def close_gripper(self):
        self.get_logger().info("Closing gripper")
        # TODO: 실제 그리퍼 닫기 명령 퍼블리시 (예: gripper_command 퍼블리셔)
        self.gripper_closed = True

    # 그리퍼 열기 (놓기)
    def open_gripper(self):
        self.get_logger().info("Opening gripper")
        # TODO: 실제 그리퍼 열기 명령 퍼블리시
        self.gripper_closed = False

    # 로봇 우측 90도 회전 (cmd_vel 퍼블리시)
    def rotate_right_90deg(self):
        self.get_logger().info("Rotating right 90 degrees")
        twist = Twist()
        twist.linear.x = 0.0
        twist.angular.z = -self.rotation_speed  # 우측 회전은 음수

        start_time = self.get_clock().now()
        duration = self.rotation_time_90deg

        while (self.get_clock().now() - start_time).nanoseconds / 1e9 < duration:
            self.cmd_vel_publisher.publish(twist)
            rclpy.spin_once(self, timeout_sec=0.1)

        # 정지 명령
        twist.angular.z = 0.0
        self.cmd_vel_publisher.publish(twist)
        self.get_logger().info("Rotation complete")

    def pick_and_place_sequence(self):
        self.get_logger().info("Starting pick and place sequence")
        self.armrun = True

        x = self.aruco_position['x']
        y = self.aruco_position['y']
        z = min(max(2.09 * self.aruco_position['z'] - 5.55,
                    self.workspace_bounds['z'][0]), self.workspace_bounds['z'][1])

        if not (self.workspace_bounds['x'][0] <= x <= self.workspace_bounds['x'][1] and
                self.workspace_bounds['y'][0] <= y <= self.workspace_bounds['y'][1] and
                self.workspace_bounds['z'][0] <= z <= self.workspace_bounds['z'][1]):
            self.get_logger().error("Marker position out of bounds")
            self.armrun = False
            return

        # 1) 집기 위치로 이동
        success = self.ik_controller.move_to_pose(x, y, z)
        if not success:
            self.get_logger().error("Arm failed to move to pick position")
            self.armrun = False
            return

        # 2) 그리퍼 닫기
        self.close_gripper()

        # 3) 초기 위치로 복귀
        self.get_logger().info("Returning to initial position with object")
        self.move_to_initial_position()

        # 4) 로봇 우측 90도 회전
        self.rotate_right_90deg()

        # 5) 내려놓기 위치로 이동 (같은 x, y, z에 내려놓는다고 가정)
        self.get_logger().info("Moving arm to place position")
        success = self.ik_controller.move_to_pose(x, y, z)
        if not success:
            self.get_logger().error("Arm failed to move to place position")
            self.armrun = False
            return

        # 6) 그리퍼 열기
        self.open_gripper()

        # 7) 초기 위치로 복귀
        self.get_logger().info("Returning to initial position after placing object")
        self.move_to_initial_position()

        self.get_logger().info("Pick and place sequence completed")
        self.task_done()
        self.armrun = False

def main(args=None):
    rclpy.init(args=args)
    node = ArucoMarkerListener()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.get_logger().info("Shutting down node")
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
