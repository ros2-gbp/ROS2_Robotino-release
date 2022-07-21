from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='robotino_ros2',
            namespace='robotino',
            executable='power_node',
            name='main'
        ),
        Node(
            package='robotino_ros2',
            namespace='robotino',
            executable='controller_node',
            name='main'
        ),
        Node(
            package='robotino_ros2',
            namespace='robotino',
            executable='service_node',
            name='main'
        ),
        Node(
            package='robotino_ros2',
            namespace='robotino',
            executable='io_node',
            name='main'
        )
    ])