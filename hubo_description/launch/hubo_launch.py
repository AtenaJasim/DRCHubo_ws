from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription, ExecuteProcess
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare
from launch_ros.actions import Node
from launch.substitutions import Command
from launch_ros.parameter_descriptions import ParameterValue
import os

def generate_launch_description():
    ld = LaunchDescription()

    ld.add_action(
        ExecuteProcess(
            cmd=[
                'gazebo',
                '--verbose',
                '-s',
                'libgazebo_ros_factory.so'
            ],
            output='screen'
        )
    )
    
    packagePath = FindPackageShare('hubo_description')

    ld.add_action(
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            parameters=[{
                'robot_description': ParameterValue(
                    Command([
                        ' xacro ',
                        PathJoinSubstitution([packagePath,'urdf', 'hubo_and_gripper_copy.urdf'])
                    ]), 
                    value_type=str
                ),
            }]
        )
    )


    ld.add_action(
        Node(
            package='gazebo_ros',
            executable='spawn_entity.py',
            output='screen',
            arguments=[
                '-topic', '/robot_description',
                '-entity', 'hubo'
            ]
        )
    )

    return ld