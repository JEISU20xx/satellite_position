#!/usr/bin/python3

# SPDX-FileCopyrightText: 2025 Junya Wada
# SPDX-License-Identifier: BSD-3-Clause

import os
import rclpy
from rclpy.node import Node
import requests
from std_msgs.msg import Float32

class SatellitePositionNode(Node):
    def __init__(self):
        super().__init__('satellite_position_node')
        self.lat_pub = self.create_publisher(Float32, 'satellite_latitude', 10)
        self.lon_pub = self.create_publisher(Float32, 'satellite_longitude', 10)
        self.alt_pub = self.create_publisher(Float32, 'satellite_altitude', 10)
        self.create_timer(5.0, self.cb)
        self.api_key = os.getenv('N2YO_API_KEY')
        self.satellite_id = '25544' # NORAD ID

    def cb(self):
        url = f'https://api.n2yo.com/rest/v1/satellite/positions/{self.satellite_id}/0/0/0/1/&apiKey={self.api_key}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            positions = data.get('positions', [])
            position = positions[0]
            lat = Float32()
            lon = Float32()
            alt = Float32()
            lat.data = position['satlatitude']
            lon.data = position['satlongitude']
            alt.data = position['sataltitude'] # km
            self.lat_pub.publish(lat)
            self.lon_pub.publish(lon)
            self.alt_pub.publish(alt)
def main():
    rclpy.init()
    node = SatellitePositionNode()
    rclpy.spin(node)

if __name__ == '__main__':
    main()
