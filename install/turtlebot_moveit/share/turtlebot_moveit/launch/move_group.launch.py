#!/usr/bin/env python3
#
# Authors: Hye-jong KIM

import os
import yaml
import xacro

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory


def generate_launch_description():
    # Robot description (URDF)
    robot_description_config = xacro.process_file(
        os.path.join(
            get_package_share_directory("turtlebot3_manipulation_description"),
            "urdf",
            "turtlebot3_manipulation.urdf.xacro",
        )
    )
    robot_description = {"robot_description": robot_description_config.toxml()}

    # Semantic description (SRDF)
    srdf_path = os.path.join(
        get_package_share_directory("turtlebot3_manipulation_moveit_config"),
        "config",
        "turtlebot3_manipulation.srdf",
    )
    with open(srdf_path, "r") as file:
        robot_description_semantic = {
            "robot_description_semantic": file.read()
        }

    # Kinematics
    kinematics_path = os.path.join(
        get_package_share_directory("turtlebot3_manipulation_moveit_config"),
        "config",
        "kinematics.yaml",
    )
    with open(kinematics_path, "r") as file:
        kinematics_yaml = yaml.safe_load(file)

    # OMPL planning pipeline
    ompl_config = {
        "move_group": {
            "planning_plugin": "ompl_interface/OMPLPlanner",
            "request_adapters": """default_planner_request_adapters/AddTimeOptimalParameterization \
default_planner_request_adapters/FixWorkspaceBounds \
default_planner_request_adapters/FixStartStateBounds \
default_planner_request_adapters/FixStartStateCollision \
default_planner_request_adapters/FixStartStatePathConstraints""",
            "start_state_max_bounds_error": 0.1,
        }
    }
    ompl_path = os.path.join(
        get_package_share_directory("turtlebot3_manipulation_moveit_config"),
        "config",
        "ompl_planning.yaml",
    )
    with open(ompl_path, "r") as file:
        ompl_yaml = yaml.safe_load(file)
    ompl_config["move_group"].update(ompl_yaml)

    # Trajectory execution
    trajectory_execution = {
        "moveit_manage_controllers": True,
        "trajectory_execution.allowed_execution_duration_scaling": 1.2,
        "trajectory_execution.allowed_goal_duration_margin": 0.5,
        "trajectory_execution.allowed_start_tolerance": 0.05,
    }

    # Controllers
    controllers_path = os.path.join(
        get_package_share_directory("turtlebot3_manipulation_moveit_config"),
        "config",
        "moveit_controllers.yaml",
    )
    with open(controllers_path, "r") as file:
        controllers_yaml = yaml.safe_load(file)
    moveit_controllers = {
        "moveit_simple_controller_manager": controllers_yaml,
        "moveit_controller_manager": "moveit_simple_controller_manager/MoveItSimpleControllerManager",
    }

    # Planning scene monitor parameters
    planning_scene_monitor = {
        "publish_planning_scene": True,
        "publish_geometry_updates": True,
        "publish_state_updates": True,
        "publish_transforms_updates": True,
        "publish_robot_description": True,
        "publish_robot_description_semantic": True
    }

    # Launch description
    ld = LaunchDescription()

    # Declare use_sim
    use_sim = LaunchConfiguration("use_sim")
    declare_use_sim = DeclareLaunchArgument(
        "use_sim", default_value="true", description="Start robot in Gazebo simulation."
    )
    ld.add_action(declare_use_sim)

    # Move group node (필수)
    move_group = Node(
        package="moveit_ros_move_group",
        executable="move_group",
        output="screen",
        parameters=[
            robot_description,
            robot_description_semantic,
            kinematics_yaml,
            ompl_config,
            trajectory_execution,
            moveit_controllers,
            planning_scene_monitor,
            {"use_sim_time": use_sim},
        ],
    )
    ld.add_action(move_group)

    # Your custom arm controller
    arm_controller_node = Node(
        package="turtlebot_moveit",
        executable="turtlebot_arm_controller",
        output="screen",
        parameters=[
            robot_description,
            robot_description_semantic,
            kinematics_yaml,
            ompl_config,
            trajectory_execution,
            moveit_controllers,
            planning_scene_monitor,
            {"use_sim_time": use_sim},
        ],
    )
    ld.add_action(arm_controller_node)

    return ld
