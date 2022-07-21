import rclpy
from rclpy.node import Node
from robotino_ros2.config import ip_address
from robotino_ros2_msg.srv import Services
from robotino_ros2_msg.msg import Service,ServiceGroup
import requests


ip = 'http://' + ip_address


class ServiceNode(Node):
    def __init__(self):
        super().__init__('service_node')
        self.services_srv = self.create_service(
            Services, 'Services', callback=self.get_controller_info)

    def get_controller_info(self, request, response):
        result = requests.get(ip + '/data/services').json()
        response_array = []
        for sub_service_group in result:
            service_group_array = []
            #get service group and loop through it
            service_group = sub_service_group['_children']
            for sub_service in service_group:
                service = Service()
                if sub_service['activation'] == 'true':
                    service.activation = True
                else:
                    service.activation = False
                service.active = sub_service['active']
                service.id = sub_service['id']
                service.name = sub_service['name']
                service.sub = sub_service['sub']
                service_group_array.append(service)
            service_group_msg = ServiceGroup()
            service_group_msg.sub_services = service_group_array
            service_group_msg.name = sub_service_group['name']
            response_array.append(service_group_msg)
        response.services = response_array
        return response

        return response

def main(args=None):
    rclpy.init(args=args)
    node = ServiceNode()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == '__main__':
    main()
