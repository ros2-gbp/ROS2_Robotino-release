import rclpy
from rclpy.node import Node
from robotino_ros2.config import ip_address
from robotino_ros2_msg.srv import ControllerInfo
import requests


ip = "http://" + ip_address


class ControllerNode(Node):
    def __init__(self):
        super().__init__("controller_node")
        self.controller_info_srv = self.create_service(
            ControllerInfo, 'controller_info', callback=self.get_controller_info)

    def get_controller_info(self, request, response):
        result = requests.get(ip + "/data/controllerinfo").json()
        response.type = result["TYPE"]
        response.hardware_payload = result["payload"]["hardware"]
        response.software_payload = result["payload"]["software"]
        return response

def main(args=None):
    rclpy.init(args=args)
    node = ControllerNode()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == '__main__':
    main()
