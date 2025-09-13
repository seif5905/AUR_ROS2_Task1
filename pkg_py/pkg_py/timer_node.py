import rclpy
from rclpy.node import Node

class Mynode(Node):
    def __init__(self):
        super().__init__("timer_node")
        self.get_logger().info("Node has started")
        self.counter = 10
        self.timing = self.create_timer(1,self.timer_callback)

    def timer_callback(self):
        if self.counter == -1:
            self.get_logger().info("Time is up!")
            self.timing.cancel()
            self.destroy_node()
        else:
            self.get_logger().info(f"Timer: {self.counter}")
            self.counter -= 1

def main(args=None):
    rclpy.init(args=args)
    node = Mynode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()