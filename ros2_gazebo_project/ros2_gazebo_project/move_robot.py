import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import math
import time

class MoveRobot(Node):
    def __init__(self):
        super().__init__('move_robot')
        self.publisher_ = self.create_publisher(Twist, '/cmd_vel', 10)
        timer_period = 0.1  # 10Hz
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.start_time = time.time()
        self.get_logger().info('MoveRobot node started — robot will move in circle')

    def timer_callback(self):
        msg = Twist()

        # Durasi putar + maju 20 detik, lalu berhenti
        elapsed = time.time() - self.start_time
        if elapsed < 20.0:
            msg.linear.x = 0.2   # maju pelan
            msg.angular.z = 0.4  # belok kiri pelan
        else:
            msg.linear.x = 0.0
            msg.angular.z = 0.0

        self.publisher_.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = MoveRobot()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
