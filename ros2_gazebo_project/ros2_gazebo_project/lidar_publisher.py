import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan

class LidarPublisher(Node):
    def __init__(self):
        super().__init__('lidar_publisher')
        self.subscription = self.create_subscription(
            LaserScan,
            '/scan',  # topic dari LIDAR Gazebo
            self.listener_callback,
            10)
        self.publisher_ = self.create_publisher(LaserScan, 'lidar_data', 10)
        self.get_logger().info('Lidar Publisher node started, listening to /scan')

    def listener_callback(self, msg):
        # Forward data ke topic baru
        self.publisher_.publish(msg)
        self.get_logger().info(f'Published LIDAR data with {len(msg.ranges)} points')

def main(args=None):
    rclpy.init(args=args)
    node = LidarPublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
