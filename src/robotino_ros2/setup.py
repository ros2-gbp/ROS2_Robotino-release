import os
from glob import glob
from setuptools import setup

package_name = 'robotino_ros2'

setup(
    name=package_name,
    version='1.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.launch.py')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Robohouse',
    maintainer_email='ziang.qiu@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'omnidrive_node = robotino_ros2.omnidrive_node:main',
            'power_node = robotino_ros2.power_node:main',
            'controller_node = robotino_ros2.controller_node:main',
            'service_node = robotino_ros2.service_node:main',
            'io_node = robotino_ros2.io_node:main',
            'camera_node = robotino_ros2.camera_node:main'
        ],
    },
)
