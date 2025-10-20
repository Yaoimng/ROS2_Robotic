from setuptools import find_packages, setup

package_name = 'ros2_gazebo_project'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='jekiijekk',
    maintainer_email='jekiijekk@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
		'lidar_publisher = ros2_gazebo_project.lidar_publisher:main',
        	'lidar_subscriber = ros2_gazebo_project.lidar_subscriber:main',
		'move_robot = ros2_gazebo_project.move_robot:main',
        ],
    },
)
