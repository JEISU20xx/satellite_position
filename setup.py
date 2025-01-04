from setuptools import setup
import os
from glob import glob

package_name = 'satellite_position'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share',package_name), glob('launch/*.launch.py')),
    ],
    install_requires=['setuptools', 'requests'],
    zip_safe=True,
    maintainer='Junya Wada',
    maintainer_email='s23c1148re@s.chibakoudai.jp',
    description='ROS2 package to fetch satellite position from NASA API and send it to another program',
    license='BSD-3-Clause',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'fetch_position = satellite_position.fetch_position:main',
        ],
    },
)
