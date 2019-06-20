#!/usr/bin/env python

import rospy
from std_msgs.msg import String
from std_msgs.msg import Float32
import numpy as np

pub = rospy.Publisher('odCmd', Float32, queue_size=10)

def od_callback(data):
	rospy.loginfo('I heard %s', data.data)
	countSpeed = data.data * (8192 / (2 * np.pi))
	rospy.loginfo('The count speed is %s', countSpeed)

def od_node():
	rospy.init_node('od_node', anonymous=True)

	# rospy.Subscriber('angle', theta, callback)
	rospy.Subscriber('velCmd', Float32, od_callback)

	# while not rospy.is_shutdown():
 #        velF = k * (tF_des - tF_act)
 #        rospy.loginfo(velF)
 #        pub.publish(velF)
 #        rate.sleep()

 	rospy.spin()
	


if __name__ == '__main__':
	# try:
	# 	od_node()
	# except rospy.ROSInterruptException:
	# 	pass
	od_node()

