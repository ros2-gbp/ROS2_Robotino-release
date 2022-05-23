import rclpy
from rclpy.node import Node
from robotino_ros2_msg.srv import PowerManagement

import requests
class PowerNode(Node):
    def __init__(self):
        super().__init__("power_node")
        self.power_management_srv = self.create_service(PowerManagement,'power_management',callback=self.get_power_management)
    
    def get_power_management(self,request,response):
        x = requests.get("http://10.42.0.148/data/powermanagement")
        print(x)

def main(args=None):
    rclpy.init(args=args)
    node = PowerNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()