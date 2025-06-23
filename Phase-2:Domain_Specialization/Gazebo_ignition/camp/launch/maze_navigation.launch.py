#!/usr/bin/env python3

import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare


def generate_launch_description():
    # Get the package directory
    pkg_dir = get_package_share_directory('camp')
    
    # Path to maze world file
    world_file = PathJoinSubstitution([
        FindPackageShare('camp'),
        'worlds',
        'maze.sdf'
    ])
    
    # Path to the URDF file
    urdf_file = os.path.join(pkg_dir, 'models', 'husky_robot_model', 'model.urdf')
    
    # Read the URDF file
    with open(urdf_file, 'r') as infp:
        robot_description_content = infp.read()

    # Robot description parameter
    robot_description = {'robot_description': robot_description_content}

    # Gazebo launch with model path
    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            PathJoinSubstitution([
                FindPackageShare('ros_gz_sim'),
                'launch',
                'gz_sim.launch.py'
            ])
        ]),
        launch_arguments={
            'gz_args': world_file
        }.items()
    )

    # Robot state publisher node
    robot_state_publisher_node = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        name='robot_state_publisher',
        output='screen',
        parameters=[robot_description, {'use_sim_time': True}]
    )

    # Joint state publisher node
    joint_state_publisher_node = Node(
        package='joint_state_publisher',
        executable='joint_state_publisher',
        name='joint_state_publisher',
        output='screen',
        parameters=[{'use_sim_time': True}]
    )

    # Spawn robot in Gazebo at a specific location in the maze
    spawn_entity = Node(
        package='ros_gz_sim',
        executable='create',
        arguments=[
            '-topic', 'robot_description',
            '-name', 'husky_robot',
            '-x', '-8.0',
            '-y', '8.0', 
            '-z', '0.5'
        ],
        output='screen'
    )

    # Bridge for essential topics
    bridge_topics = [
        '/clock@rosgraph_msgs/msg/Clock[gz.msgs.Clock',
        '/cmd_vel@geometry_msgs/msg/Twist@gz.msgs.Twist',
        '/odom@nav_msgs/msg/Odometry@gz.msgs.Odometry',
        '/tf@tf2_msgs/msg/TFMessage@gz.msgs.Pose_V',
    ]

    bridge_node = Node(
        package='ros_gz_bridge',
        executable='parameter_bridge',
        arguments=bridge_topics,
        output='screen'
    )

    return LaunchDescription([
        gazebo,
        robot_state_publisher_node,
        joint_state_publisher_node,
        spawn_entity,
        bridge_node
    ])
