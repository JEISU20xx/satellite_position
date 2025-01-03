#!/bin/bash

# SPDX-FileCopyrightText: 2025 Junya Wada
# SPDX-License-Identifier: BSD-3-Clause

dir=~
[ "$1" != "" ] && dir="$1"

cd $dir/ros2_ws
colcon build
source $dir/.bashrc
timeout 10 ros2 run satellite_position fetch_position > /tmp/log
cat /tmp/log |
grep 'Published satellite position'