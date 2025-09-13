#!usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32
import random

class MyNode(Node):
    def __init__(self):
        super().__init__("humidity_node")
        self.temp = self.create_publisher(Int32, "humidity", 10)
        self.timer = self.create_timer(1,self.send_humid)
        self.get_logger().info("humidity node has started")

    def send_humid(self):
        msg = Int32()
        msg.data = random.randint(20,100)
        self.get_logger().info(f"Humidity = {msg.data} %")
        self.temp.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = MyNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()