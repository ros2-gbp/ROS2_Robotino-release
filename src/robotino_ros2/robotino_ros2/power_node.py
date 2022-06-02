import rclpy
from rclpy.node import Node
from robotino_ros2_msg.srv import PowerManagement

import requests
class PowerNode(Node):
    def __init__(self):
        super().__init__("power_node")
        self.power_management_srv = self.create_service(PowerManagement,'power_management',callback=self.get_power_management)
    
    def get_power_management(self,request,response):
        print("got request")
        result = requests.get("http://10.42.0.148/data/powermanagement").json()
        print(result)
        response.battery_low = result["batteryLow"]
        response.battery_low_shutdown_counter = result["batteryLowShutdownCounter"]
        response.battery_type = result["batteryType"]
        response.ext_power = result["ext_power"]
        response.num_chargers = result["num_chargers"]
        response.voltage = result["voltage"]
        return response


def main(args=None):
    rclpy.init(args=args)
    node = PowerNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()