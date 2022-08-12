# ROS2_Robotino
ROS2 package for robotino.
Fully redesigned package that adapts to robotino [RestAPI](!https://wiki.openrobotino.org/index.php?title=Rest_api).

## Prerequisite

To run this package, you have to install these system components first.
- [Robotino4 OS](!https://wiki.openrobotino.org/index.php?title=Robotino4_images)
- [ROS Galactic](!https://docs.ros.org/en/galactic/Installation.html)

Use other version is at your **OWN** risk, they are **NOT** tested with this system.
Ubuntu 20.04 is **STRONGLY** recommended for this package.

### Install LiDAR and Camera Dependencies on robotino
Connect robotino with ssh protocol \
`sshpass -p robotino robotino@robotino_ip_address`

Clone this repository by \
`git clone https://github.com/SkyloveQiu/ROS2_Robotino.git`

Install dependencies by \
`./install.sh`

config your robotino ip in [config file](!src/robotino_ros2/robotino_ros2/config.py)


build your robot by \
`colcon build`

install your ros package by \
`source install/setup.bash` 
or 
`source install/setup.zsh`

config network connection by \
`export ROS_DOMAIN_ID=1`

launch camera and laser node on the robotino by \
`ros2 launch robotino_ros2 robotino_local`

launch other nodes on your computer by \
`ros2 launch robotino_ros2 robotino_remote`

You can try to control robotino by teleop \
`ros2 run teleop_twist_keyboard teleop_twist_keyboard`

## run script
To run this project faster, a run script has been finished. use `./run.zsh` to run this project.


## Contributing

Interested in contributing to the Robotino project? Thanks so much for your interest! We are always looking for improvements to the project and contributions from open-source developers are greatly appreciated.

