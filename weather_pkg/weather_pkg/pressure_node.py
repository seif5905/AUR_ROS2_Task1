#!usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32
import random

class MyNode(Node):
    def __init__(self):
        super().__init__("pressure_node")
        self.temp = self.create_publisher(Int32, "pressure", 10)
        self.timer = self.create_timer(1,self.send_pressure)
        self.get_logger().info("pressure node has started")

    def send_pressure(self):
        msg = Int32()
        msg.data = random.randint(900,1100)
        self.get_logger().info(f"Pressure = {msg.data} hPa")
        self.temp.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = MyNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()