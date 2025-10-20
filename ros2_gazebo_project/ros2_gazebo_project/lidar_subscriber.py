import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan
import numpy as np

class LidarSubscriber(Node):
    def __init__(self):
        super().__init__('lidar_subscriber')
        self.subscription = self.create_subscription(
            LaserScan,
            'lidar_data',
            self.listener_callback,
            10)
        self.get_logger().info('Lidar Subscriber node started')

    def listener_callback(self, msg):
        ranges = np.array(msg.ranges)
        valid = ranges[np.isfinite(ranges)]
        if len(valid) > 0:
            min_distance = np.min(valid)
            self.get_logger().info(f'Closest obstacle: {min_distance:.2f} m')

def main(args=None):
    rclpy.init(args=args)
    node = LidarSubscriber()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

