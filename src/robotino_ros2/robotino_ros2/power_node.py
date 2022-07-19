import rclpy
from rclpy.node import Node
from robotino_ros2_msg.srv import PowerManagement,Charger
from configparser import ConfigParser
import requests

config = ConfigParser()
config.read('config.cfg')
ip = "http://" + config.get("internet", "ip_address")

class PowerNode(Node):
    def __init__(self):
        super().__init__("power_node")
        self.power_management_srv = self.create_service(PowerManagement,'power_management',callback=self.get_power_management)
        self.charger_srv = self.create_service(Charger, 'Charger', callback=self.get_charger_info)
    def get_power_management(self,request,response):
        result = requests.get(ip + "/data/powermanagement").json()
        response.battery_low = result["batteryLow"]
        response.battery_low_shutdown_counter = result["batteryLowShutdownCounter"]
        response.battery_type = result["batteryType"]
        response.ext_power = result["ext_power"]
        response.num_chargers = result["num_chargers"]
        response.voltage = result["voltage"]
        return response

    def get_charger_info(self,request,response):
        result = requests.get(ip + "/data/charger0").json()



def main(args=None):
    rclpy.init(args=args)
    node = PowerNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()