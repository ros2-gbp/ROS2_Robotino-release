from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='robotino_ros2',
            namespace='robotino',
            executable='power_node',
            name='power'
        ),
        Node(
            package='robotino_ros2',
            namespace='robotino',
            executable='controller_node',
            name='controller'
        ),
        Node(
            package='robotino_ros2',
            namespace='robotino',
            executable='service_node',
            name='service'
        ),
        Node(
            package='robotino_ros2',
            namespace='robotino',
            executable='io_node',
            name='io'
        ),
        Node(
            package='robotino_ros2',
            namespace='robotino',
            executable='omnidrive_node',
            name='omnidrive'
        )
    ])