import rclpy
from rclpy.node import Node
from robotino_ros2.config import ip_address
from sensor_msgs.msg import LaserScan
import requests

ip = "http://" + ip_address


class LidarNode(Node):
    def __init__(self):
        super().__init__("lidar_node")
        self.camera_publisher = self.create_publisher(LaserScan,'laser_scan',10)
        self.timer = self.create_timer(0.05, self.lidar_callback)


    def lidar_callback(self):
        msg = LaserScan()
        respones = requests.get(ip_address+"/data/distancesensorarray").json()
        if respones.contains("ranges"):
            pass
            

        

def main(args=None):
    rclpy.init(args=args)
    node = LidarNode()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == '__main__':
    main()
