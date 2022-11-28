#!/usr/bin/env python
from __future__ import absolute_import, division, print_function
import time
import rospy
import math
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
from std_msgs.msg import Int32
from sensor_msgs.msg import LaserScan
from unitysim.msg import BoundingBox3d

class RobotController:
    def __init__(self):
        pass
    def main_loop(self):
        pass
            
def main(args=None):
    rospy.init_node("Controller",anonymous=True)
    robot_controller = RobotController()
    time.sleep(2) #Sleep to allow time to initialize. Otherwise subscriber might recieve an empty message
    robot_controller.main_loop()

if __name__ == '__main__':
    main()