#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Camera Frame Capture and JPEG Compression

Author: Rujin Kim
Date: 2025-06-16
"""

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node, PushRosNamespace

def generate_launch_description():
    return LaunchDescription([

        # Declare arguments
        DeclareLaunchArgument(
            'video_port',
            default_value='0',
            description='/dev/video* 번호 (예: 0, 1, ...)'
        ),
        DeclareLaunchArgument(
            'namespace',
            default_value='camera',
            description='ROS 2 네임스페이스 지정'
        ),

        # Push namespace
        PushRosNamespace(LaunchConfiguration('namespace')),

        # 노드 실행: compressed_image_pub
        Node(
            package='aruco_yolo',
            executable='compressed_image_pub',
            name='compressed_image_pub',
            output='screen',
            parameters=[{
                'video_port': LaunchConfiguration('video_port')
            }],
            arguments=['--ros-args', '--log-level', 'INFO']
        ),

        # 노드 실행: aruco_detector
        Node(
            package='aruco_yolo',
            executable='aruco_detector',
            name='aruco_detector',
            output='screen',
            arguments=['--ros-args', '--log-level', 'INFO']
        ),
    ])
