import rclpy
from rclpy.node import Node
from robotino_ros2.config import ip_address
from robotino_ros2_msg.msg import Omnidrive
import requests
import json


ip = "http://" + ip_address


class OmnidriveNode(Node):
    def __init__(self):
        super().__init__("omnidrive_node")
        self.omnidrive_subscription = self.create_subscription(Omnidrive,'omnidriver',self.omnidrive_callback,10)
    
    def omnidrive_callback(self,msg):
        headers = {'Content-Type': 'application/json', 'Accept':'application/json'}
        request_json = [msg.vx,msg.vy,msg.omega]
        requests.post(ip+"/data/omnidrive",data=json.dumps(request_json),headers=headers)

        


def main(args=None):
    rclpy.init(args=args)
    node = OmnidriveNode()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == '__main__':
    main()
