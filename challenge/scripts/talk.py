#!/usr/bin/env python

import rospy
from rospy.topics import Publisher
## from std_msgs import msg

from challenge.msg import euler_pose

from tf.transformations import quaternion_from_euler

def talk():
    rospy.init_node('talk', anonymous=True)
    pub = rospy.Publisher('custom_talker', euler_pose, queue_size=10)
    rate = rospy.Rate(10)

    msg = euler_pose()

    while not rospy.is_shutdown():
        
        print("Enter angles in radians")
        msg.Fangle = float(raw_input("1: "))
        msg.Sangle = float(raw_input("2: "))
        msg.Tangle = float(raw_input("3: "))
        
        list = [msg.Fangle, msg.Sangle, msg.Tangle]

        q = quaternion_from_euler(list[0], list[1], list[2])
        
        message =  "The quaternion representation is %s %s %s %s." % (q[0], q[1], q[2], q[3])
        pub.publish(message)   
        rate.sleep()
    

if __name__ == "__main__":
    try:
        talk()
    except rospy.ROSInterruptException:
        pass