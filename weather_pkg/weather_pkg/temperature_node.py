#!usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32
import random

class MyNode(Node):
    def __init__(self):
        super().__init__("temperature_node")
        self.temp = self.create_publisher(Int32, "temperature", 10)
        self.timer = self.create_timer(1,self.send_temp)
        self.get_logger().info("temperature node has started")

    def send_temp(self):
        msg = Int32()
        msg.data = random.randint(15,40)
        self.get_logger().info(f"Temp = {msg.data} 'C")
        self.temp.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = MyNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()