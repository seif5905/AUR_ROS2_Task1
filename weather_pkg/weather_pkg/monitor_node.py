#!usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32



class MyNode(Node):
    def __init__(self):
        super().__init__("monitor_node")
        self.temp_sub = self.create_subscription(
                        Int32, "temperature", self.temp_callback, 10)
        self.pressure_sub = self.create_subscription(
                        Int32, "pressure", self.pressure_callback, 10)
        self.humidity_sub = self.create_subscription(
                        Int32, "humidity", self.humid_callback, 10)

    def temp_callback(self, msg):
        self.get_logger().info(f"Temp = {msg.data} 'C")
        self.log_file = open("Readings.txt", "a")
        self.log_file.write(f"Temperature = {msg.data} 'C\n")
        self.log_file.flush()
        self.log_file.close()

    def pressure_callback(self, msg):
        self.get_logger().info(f"Pressure = {msg.data} hPa")
        self.log_file = open("Readings.txt", "a")
        self.log_file.write(f"Pressure = {msg.data} hPa\n")
        self.log_file.flush()
        self.log_file.close()

    def humid_callback(self, msg):
        self.get_logger().info(f"Humidity = {msg.data} %")
        self.log_file = open("Readings.txt", "a")
        self.log_file.write(f"Humidity = {msg.data} %\n")
        self.log_file.flush()
        self.log_file.close()


def main(args=None):
    rclpy.init(args=args)
    node = MyNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()