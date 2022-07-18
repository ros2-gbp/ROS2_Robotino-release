import sys

from robotino_ros2_msg.srv import PowerManagement,Charger
import rclpy
from rclpy.node import Node

class PowerNodeClient(Node):
    def __init__(self):
        super().__init__("power_node_client")
        self.power_management_client = self.create_client(PowerManagement, "power_management")
        self.charger_client = self.create_client(Charger, "Charger")
        while not self.power_management_client.wait_for_service(timeout_sec=1.0):
            print('service not available, waiting again...')
        while not self.charger_client.wait_for_service(timeout_sec=1.0):
            print('service not available, waiting again...')
    
    def power_management_info(self):
        req = PowerManagement.Request()
        self.result = self.power_management_client.call_async(req)
        print(self.result)
    
    def charger_info(self):
        pass


def main(args=None):
    rclpy.init(args=args)
    power_node_cli = PowerNodeClient()
    power_node_cli.power_management_info()
    print(power_node_cli.result)
    power_node_cli.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

