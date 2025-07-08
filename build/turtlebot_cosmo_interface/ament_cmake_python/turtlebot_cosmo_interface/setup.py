from setuptools import find_packages
from setuptools import setup

setup(
    name='turtlebot_cosmo_interface',
    version='0.0.0',
    packages=find_packages(
        include=('turtlebot_cosmo_interface', 'turtlebot_cosmo_interface.*')),
)
