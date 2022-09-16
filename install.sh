#!/bin/sh
sudo apt update
sudo apt install libboost-all-dev ros-galactic-diagnostic-updater \
                        ros-galactic-laser-proc ros-galactic-urg-c \
                        ros-galactic-usb-cam
sudo apt install ros-galactic-urg-node-msgs
sudo apt install ros-galactic-robot-localization
sudo apt install ros-galactic-slam-toolbox
sudo apt install ros-galactic-joint-state-publisher-gui
sudo apt install ros-galactic-xacro