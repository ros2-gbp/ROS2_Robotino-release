import cv2
import rclpy
from rclpy.node import Node
from robotino_ros2.config import ip_address
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import requests
import numpy as np

ip = "http://" + ip_address


class CameraNode(Node):
    def __init__(self):
        super().__init__("camera_node")
        self.camera_publisher = self.create_publisher(Image,'camera',10)
        self.bridge = CvBridge()
        self.timer = self.create_timer(0.1, self.image_callback)


    def image_callback(self):
        response = requests.get(ip_address+"/cam0")
        if response.status_code == 200:
            self.cv_image = cv2.imread(response.content)
            msg = self.bridge.cv2_to_imgmsg(np.array(self.cv_image), "bgr8")
            self.camera_publisher.publish(msg)


def main(args=None):
    rclpy.init(args=args)
    node = CameraNode()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == '__main__':
    main()
