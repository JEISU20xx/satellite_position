#!/bin/bash -xv

# SPDX-FileCopyrightText: 2025 Junya Wada
# SPDX-License-Identifier: BSD-3-Clause

dir=~
[ "$1" != "" ] && dir="$1"

cd $dir/ros2_ws
colcon build
source $dir/.bashrc
timeout 10 ros2 launch satellite_position test.launch.py > /tmp/satellite_position.log

cat /tmp/satellite_position.log | grep 'Latitude'
cat /tmp/satellite_position.log | grep 'Longitude'
cat /tmp/satellite_position.log | grep 'Altitude'
