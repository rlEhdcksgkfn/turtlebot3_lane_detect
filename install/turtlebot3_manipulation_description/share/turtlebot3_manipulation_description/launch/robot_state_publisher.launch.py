from launch import LaunchDescription
from launch_ros.actions import Node
from launch.substitutions import Command
from launch_ros.substitutions import FindPackageShare
import os

def generate_launch_description():
    pkg_name = 'turtlebot3_manipulation_description'
    urdf_file = 'urdf/turtlebot3_manipulation.urdf.xacro'
    pkg_share = FindPackageShare(pkg=pkg_name).find(pkg_name)
    xacro_path = os.path.join(pkg_share, urdf_file)

    return LaunchDescription([
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            name='robot_state_publisher',
            output='screen',
            parameters=[{
                'robot_description': Command(['xacro ', xacro_path])
            }]
        )
    ])
