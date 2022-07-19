#!/bin/zsh

colcon build
source install/setup.zsh
ros2 launch robotino_ros2 robotino.launch.py
