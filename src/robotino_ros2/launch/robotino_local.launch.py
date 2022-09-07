from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import OpaqueFunction
from launch.actions import SetLaunchConfiguration
from launch.substitutions import LaunchConfiguration
from launch.actions import DeclareLaunchArgument

import os

from ament_index_python.packages import get_package_share_directory


def generate_launch_description():
    ld = LaunchDescription([
        DeclareLaunchArgument(
            'robotino_ros2',
            default_value = "normal",
            description='ros2 package for robotino')])

    robotino_ros2_dir = get_package_share_directory('robotino_ros2')

    # get path to params file
    params_path = os.path.join(
        robotino_ros2_dir,
        'config',
        'camera_param.yaml'
    )

    def expand_param_file_name(context):
        param_file = os.path.join(
            robotino_ros2_dir, 'config',
            'lidar_config.yaml')
        if os.path.exists(param_file):
            return [SetLaunchConfiguration('param', param_file)]

    param_file_path = OpaqueFunction(function=expand_param_file_name)
    ld.add_action(param_file_path)
    hokuyo_node = Node(
        package='urg_node', executable='urg_node', output='screen',
        name="lidar_node",
        parameters=[LaunchConfiguration('param')])

    print(params_path)
    ld.add_action(Node(
        package='usb_cam', executable='usb_cam_node_exe', output='screen',
        name="camera_node",
        # namespace=ns,
        parameters=[params_path]
    ))
    ld.add_action(hokuyo_node)
    return ld
