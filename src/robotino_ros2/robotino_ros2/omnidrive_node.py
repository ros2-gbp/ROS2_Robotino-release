import rclpy
from rclpy.node import Node
from robotino_ros2.config import ip_address
from robotino_ros2_msg.msg import Omnidrive
from geometry_msgs.msg import Twist
import requests
import json


ip = "http://" + ip_address
headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}


class OmnidriveNode(Node):
    def __init__(self):
        super().__init__("omnidrive_node")
        self.omnidrive_subscription = self.create_subscription(
            Omnidrive, 'omnidriver', self.omnidrive_callback, 10)
        self.teleop_drive_subscription = self.create_subscription(
            Twist, "/cmd_vel", self.teleop_drive_callback, 10)

    def omnidrive_callback(self, msg):
        request_json = [msg.vx, msg.vy, msg.omega]
        requests.post(ip+"/data/omnidrive",
                      data=json.dumps(request_json), headers=headers)

    def teleop_drive_callback(self, msg):
        x = msg.linear.x * 0.3
        y = msg.linear.y * 0.3
        z = msg.angular.z * 0.3
        request_json = [x, y, z]
        print(request_json)
        requests.post(ip+"/data/omnidrive",
                      data=json.dumps(request_json), headers=headers)


def main(args=None):
    rclpy.init(args=args)
    node = OmnidriveNode()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == '__main__':
    main()
