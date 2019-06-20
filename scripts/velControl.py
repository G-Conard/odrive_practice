#!/usr/bin/env python

import rospy
from std_msgs.msg import String
from std_msgs.msg import Float32
import numpy as np

pub = rospy.Publisher('velCmd', Float32, queue_size=10)
global tF_des

global tF_act
tF_act = np.pi

global k
k = 0.5

def vel_callback(data):
	tF_des = data.data
	rospy.loginfo('I heard %s', tF_des)
	


def velControl():
	rospy.init_node('velControl', anonymous=True)

	# rospy.Subscriber('angle', theta, callback)
	rospy.Subscriber('angle', Float32, vel_callback)

	# spin() simply keeps python from exiting until this node is stopped
    # rospy.spin()
	

	# pub = rospy.Publisher('velCmd', theta, queue_size=10)
	# rospy.Publisher('velCmd', Float32, queue_size=10)
	# rospy.init_node('velControl', anonymous=True)
	
	rate = rospy.Rate(100)

	while not rospy.is_shutdown():
        	velFemor = k * (tF_des - tF_act)
        rospy.loginfo(velFemor)
        pub.publish(velFemor)
        rate.sleep()





if __name__ == '__main__':
	try:
		velControl()
	except rospy.ROSInterruptException:
		pass