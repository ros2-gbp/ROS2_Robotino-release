import rclpy
import json
import requests
from rclpy.node import Node
from robotino_ros2.config import ip_address
from robotino_ros2_msg.srv import IOStatus
from robotino_ros2_msg.msg import OutputControl, OutputControlArray


ip = "http://" + ip_address


class IONode(Node):
    def __init__(self):
        super().__init__("io_node")
        self.controller_info_srv = self.create_service(
            IOStatus, 'io_status', callback=self.get_io_status)
        self.digital_output_subscriber = self.subscriptions(
            OutputControl, "digital_output_sub", self.digital_output_control, 10)
        self.digital_output_array_subscriber = self.subscriptions(
            OutputControlArray, "digital_output_array_sub", self.degital_output_array_control, 10)
        self.relay_subscriber = self.subscriptions(OutputControl, "relay_control", self.relay_control, 10)
        self.relay_array_subscriber = self.subscriptions(OutputControlArray, "relay_array_control", self.relay_array_control, 10)

    def degital_output_control(self, msg):
        request_json = {
            "num": msg.NUM,
            "val": msg.VAL
        }
        requests.post(ip+"/data/digitaloutput", data=json.dumps(request_json))

    def degital_output_array_control(self, msg):
        request_json = msg.array
        if len(request_json) == 8:
            requests.post(ip+"/data/digitaloutputarray",
                          data=json.dumps(request_json))

    def relay_control(self, msg):
        request_json = {
            "num": msg.NUM,
            "val": msg.VAL
        }
        requests.post(ip+"/data/relay", data=json.dumps(request_json))

    def relay_array_control(self, msg):
        request_json = msg.array
        if len(request_json) == 8:
            requests.post(ip+"/data/relayarray",
                          data=json.dumps(request_json))

    def get_io_status(self, request, response):
        result = requests.get(ip + "/data/analoginputarray").json()
        response.analog_input_array = result
        result = requests.get(ip + "/data/digitalinputarray").json()
        response.digital_input_array = result
        result = requests.get(ip + "/data/digitaloutputstatus").json()
        response.digital_output_array = result
        return response


def main(args=None):
    rclpy.init(args=args)
    node = IONode()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == '__main__':
    main()
