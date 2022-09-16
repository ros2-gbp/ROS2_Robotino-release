import rclpy
from rclpy.node import Node
from robotino_ros2.config import ip_address
from robotino_ros2_msg.srv import ControllerInfo
import requests
import tf2_ros
from nav_msgs.msg import Odometry
from geometry_msgs.msg import TransformStamped
import math
import datetime

ip = "http://" + ip_address
def quaternion_from_euler(roll, pitch, yaw):
    """
    Converts euler roll, pitch, yaw to quaternion (w in last place)
    quat = [x, y, z, w]
    Bellow should be replaced when porting for ROS 2 Python tf_conversions is done.
    """
    cy = math.cos(yaw * 0.5)
    sy = math.sin(yaw * 0.5)
    cp = math.cos(pitch * 0.5)
    sp = math.sin(pitch * 0.5)
    cr = math.cos(roll * 0.5)
    sr = math.sin(roll * 0.5)

    q = [0] * 4
    q[0] = cy * cp * cr + sy * sp * sr
    q[1] = cy * cp * sr - sy * sp * cr
    q[2] = sy * cp * sr + cy * sp * cr
    q[3] = sy * cp * cr - cy * sp * sr

    return q

class ControllerNode(Node):
    def __init__(self):
        super().__init__("controller_node")
        self.controller_info_srv = self.create_service(
            ControllerInfo, 'controller_info', callback=self.get_controller_info)
        self.odom_pub = self.create_publisher(Odometry,"odom",50)
        self.broadcaster = tf2_ros.TransformBroadcaster(self, 10)
        self.odometry = Odometry()
        while True:
            self.odometry_callback()

    def get_controller_info(self, request, response):
        result = requests.get(ip + "/data/controllerinfo").json()
        response.type = result["TYPE"]
        response.hardware_payload = result["payload"]["hardware"]
        response.software_payload = result["payload"]["software"]
        return response

    def odometry_callback(self):
        try:
            result = requests.get(ip + "/data/odometry").json()
            x = result[0]
            y = result[1]
            rot = result[2]
            vx = result[3]
            vy = result[4]
            omega = result[5]
            seq = result[6]
            self.odometry.header.stamp = self.get_clock().now().to_msg()
            self.odometry.header.frame_id = "odom"
            self.odometry.pose.pose.position.x = float(x)
            self.odometry.pose.pose.position.y = float(y)
            self.odometry.pose.pose.position.z = 0.0
            result = quaternion_from_euler(rot,0,math.pi)
            self.odometry.pose.pose.orientation.x = result[0]
            self.odometry.pose.pose.orientation.y = result[1]
            self.odometry.pose.pose.orientation.z = result[2]
            self.odometry.pose.pose.orientation.w = result[3] 
            self.odometry.twist.twist.linear.x = float(vx)
            self.odometry.twist.twist.linear.y = float(vy)
            self.odometry.twist.twist.linear.z = 0.0
            self.odometry.twist.twist.linear.z = 0.0
            self.odometry.twist.twist.angular.x = 0.0
            self.odometry.twist.twist.angular.y = 0.0
            self.odometry.twist.twist.angular.z = float(omega)
            self.odometry.child_frame_id = 'base_link'
            self.odom_pub.publish(self.odometry)

            odom_trans = TransformStamped()
            odom_trans.header.frame_id = 'odom'
            odom_trans.child_frame_id = 'base_link'
            odom_trans.header.stamp = self.get_clock().now().to_msg()
            odom_trans.transform.translation.x = self.odometry.pose.pose.position.x
            odom_trans.transform.translation.y = self.odometry.pose.pose.position.y
            odom_trans.transform.translation.z = self.odometry.pose.pose.position.z
            odom_trans.transform.rotation = self.odometry.pose.pose.orientation     #includes x,y,z,w
            self.broadcaster.sendTransform(odom_trans)
        finally:
            return
        
   
        

def main(args=None):
    print("init the controller node")
    rclpy.init(args=args)
    node = ControllerNode()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == '__main__':
    main()
