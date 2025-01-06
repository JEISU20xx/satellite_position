#!/usr/bin/python3

# SPDX-FileCopyrightText: 2025 Junya Wada
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class ListenPositionNode(Node):
    def __init__(self):
        super().__init__('receive_position')
        self.subscription = self.create_subscription(
            String,
            'satellite_position',
            self.listener_callback,
            10)

    def listener_callback(self, msg):
        self.get_logger().info(f'Received satellite position: {msg.data}')

def main(args=None):
    rclpy.init(args=args)
    node = ListenPositionNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
