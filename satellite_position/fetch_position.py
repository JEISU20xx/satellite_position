#!/usr/bin/python3

# SPDX-FileCopyrightText: 2025 Junya Wada
# SPDX-License-Identifier: BSD-3-Clause

import os
import rclpy
from rclpy.node import Node
import requests
from std_msgs.msg import String

class SatellitePositionNode(Node):
    def __init__(self):
        super().__init__('satellite_position_node')
        self.pub = self.create_publisher(String, 'satellite_position', 10)
        self.create_timer(5.0, self.cb)
        self.api_key = os.getenv('N2YO_API_KEY')
        self.satellite_id = '25544'

    def cb(self):
        url = f'https://api.n2yo.com/rest/v1/satellite/positions/{self.satellite_id}/0/0/0/1/&apiKey={self.api_key}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            positions = data.get('positions', [])
            if positions:
                position = positions[0]
                msg = String()
                msg.data = f"Lat: {position['satlatitude']}, Lon: {position['satlongitude']}, Alt: {position['sataltitude']}"
                self.pub.publish(msg)
                self.get_logger().info(f'Published satellite position: {msg.data}')
            else:
                self.get_logger().error('No position data available')
        else:
            self.get_logger().error('Failed to fetch data from N2YO API')

def main():
    rclpy.init()
    node = SatellitePositionNode()
    rclpy.spin(node)

if __name__ == '__main__':
    main()
