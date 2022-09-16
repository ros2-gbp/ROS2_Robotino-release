#!/bin/sh
sudo apt update
sudo apt install libboost-all-dev ros-humble-diagnostic-updater \
                        ros-humble-laser-proc ros-humble-urg-c \
                        ros-humble-usb-cam
sudo apt install ros-humble-urg-node-msgs
sudo apt install ros-humble-robot-localization
sudo apt install ros-humble-slam-toolbox
sudo apt install ros-humble-joint-state-publisher-gui
sudo apt install ros-humble-xacro