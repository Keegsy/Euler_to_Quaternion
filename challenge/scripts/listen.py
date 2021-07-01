#!/usr/bin/env python

import rospy
from challenge.msg import euler_pose

def listen_back(data):
    rospy.loginfo(data.data)

    
def listen():
    rospy.init_node('listen', anonymous=True)
    rospy.Subscriber('custom_talker', euler_pose, listen_back)
    rospy.spin()

if __name__ == '__main__':
    listen()
