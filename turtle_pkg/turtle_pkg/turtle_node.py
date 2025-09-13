import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import sys
import termios
import tty
import select


class TeleopTurtleWASD(Node):
    def __init__(self):
        super().__init__('teleop_turtle_wasd')
        self.publisher_ = self.create_publisher(Twist, 'turtle2/cmd_vel', 10)
        self.get_logger().info("Control turtle2 using WASD keys (press q to quit)")
        self.key_loop()

    def key_loop(self):
        while rclpy.ok():
            key = self.get_key()
            twist = Twist()

            if key.lower() == 'w':      # Forward
                twist.linear.x = 2.0
            elif key.lower() == 's':    # Backward
                twist.linear.x = -2.0
            elif key.lower() == 'a':    # Left
                twist.angular.z = 2.0
            elif key.lower() == 'd':    # Right
                twist.angular.z = -2.0
            elif key.lower() == 'q':    # Quit
                break
            else:
                twist.linear.x = 0.0
                twist.angular.z = 0.0

            self.publisher_.publish(twist)

    def get_key(self):
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            rlist, _, _ = select.select([sys.stdin], [], [], 0.1)
            if rlist:
                key = sys.stdin.read(1)
            else:
                key = ''
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return key


def main(args=None):
    rclpy.init(args=args)
    node = TeleopTurtleWASD()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
