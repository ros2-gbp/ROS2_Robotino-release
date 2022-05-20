cmake_minimum_required(VERSION 3.8)
project(robotino_ros2_msg)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
# uncomment the following section in order to fill in
# further dependencies manually.
# find_package(<dependency> REQUIRED)
find_package(ament_cmake REQUIRED)
find_package(rosidl_default_generators REQUIRED)
find_package(builtin_interfaces REQUIRED)
find_package(geometry_msgs REQUIRED)
rosidl_generate_interfaces(${PROJECT_NAME}
  "msg/AnalogReadings.msg"
  "msg/EncoderReadings.msg"
  "msg/MotorReadings.msg"
  "msg/SetBHAPressures.msg"
  "msg/BHAReadings.msg"
  "msg/GrapplerReadings.msg"
  "msg/NorthStarReadings.msg"
  "msg/SetGrapplerAxes.msg"
  "msg/DigitalReadings.msg"
  "msg/GripperState.msg"
  "msg/PowerReadings.msg"
  "msg/SetGrapplerAxis.msg"
  "srv/ResetOdometry.srv"
  "srv/SetEncoderPosition.srv"
  "srv/SetGripperState.srv"
  DEPENDENCIES builtin_interfaces
  DEPENDENCIES geometry_msgs
)

if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  # the following line skips the linter which checks for copyrights
  # comment the line when a copyright and license is added to all source files
  set(ament_cmake_copyright_FOUND TRUE)
  # the following line skips cpplint (only works in a git repo)
  # comment the line when this package is in a git repo and when
  # a copyright and license is added to all source files
  set(ament_cmake_cpplint_FOUND TRUE)
  ament_lint_auto_find_test_dependencies()
endif()

ament_package()
