#!/bin/sh
sudo update
sudo apt-get install libboost-all-dev ros-galactic-diagnostic-updater \
                        ros-galactic-laser-proc ros-galactic-urg-c \
                        ros-galactic-usb-cam
sudo apt install ros-galactic-urg-node-msgs