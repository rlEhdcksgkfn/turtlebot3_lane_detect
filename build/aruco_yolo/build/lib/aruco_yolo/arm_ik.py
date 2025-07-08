import numpy as np
from visual_kinematics.RobotSerial import RobotSerial
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint
from std_msgs.msg import Header

dh_params = np.array([
    [0.0,     0.017,     0.5*np.pi, 0.0],
    [0.0,     0.0595,    0.0,       0.0],
    [0.024,   0.128,     0.0,       0.0],
    [0.124,   0.0,      -0.5*np.pi, 0.0],
])

class ArmIKController:
    def __init__(self, joint_pub):
        self.robot = RobotSerial(dh_params)
        self.joint_pub = joint_pub
        self.joint_names = ['joint1', 'joint2', 'joint3', 'joint4']

    def move_to_pose(self, x, y, z):
        T = np.eye(4)
        T[:3, 3] = [x, y, z]

        sol = self.robot.inverse(T)
        if sol is None:
            print("역기구학 해 찾기 실패")
            return False

        joint_angles = sol[0]

        traj_msg = JointTrajectory()
        traj_msg.header = Header()
        traj_msg.joint_names = self.joint_names

        point = JointTrajectoryPoint()
        point.positions = joint_angles[:4].tolist()
        point.time_from_start.sec = 2

        traj_msg.points.append(point)
        self.joint_pub.publish(traj_msg)

        print(f"목표 위치로 이동: {x}, {y}, {z} -> 조인트 각도: {joint_angles[:4]}")

        return True
