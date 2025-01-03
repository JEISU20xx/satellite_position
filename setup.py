from setuptools import setup

package_name = 'satellite_position'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
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
