#!/usr/bin/python3

# SPDX-FileCopyrightText: 2025 Junya Wada
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32 

class ListenPositionNode(Node):
    def __init__(self):
        super().__init__('receive_position')
        self.lat_sub = self.create_subscription(Float32,'satellite_latitude',self.lat_cb,10)
        self.lon_sub = self.create_subscription(Float32,'satellite_longitude',self.lon_cb,10)
        self.alt_sub = self.create_subscription(Float32,'satellite_altitude',self.alt_cb,10)

    def lat_cb(self, msg):
        self.get_logger().info(f'Latitude: {msg.data}')
    def lon_cb(self, msg):
        self.get_logger().info(f'Longitude:{msg.data}')
    def alt_cb(self, msg):
        self.get_logger().info(f'Altitude:{msg.data}')

def main(args=None):
    rclpy.init(args=args)
    node = ListenPositionNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
