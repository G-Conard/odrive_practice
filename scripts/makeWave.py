#!/usr/bin/env python

import rospy
from std_msgs.msg import String
from std_msgs.msg import Float32
import numpy as np


def makeWave():
	pub = rospy.Publisher('sineWave', Float32, queue_size=10)
	rospy.init_node('makeWave', anonymous=True)
	rate = rospy.Rate(100)
	
	x = 1.
	y = 0.
	theta = 0.
	omega = 2 * np.pi * 2
	while not rospy.is_shutdown():
		x = 15000*np.cos(theta)
		#y = np.sin(theta)

		rospy.loginfo(x)
		pub.publish(x)

		theta = theta + omega * 0.01
		rate.sleep()

if __name__ == '__main__':
	try:
		makeWave()
	except rospy.ROSInterruptException:
		pass




# Your Parameters
#amp = 1         # 1V        (Amplitude)
#f = 1000        # 1kHz      (Frequency)
#fs = 200000     # 200kHz    (Sample Rate)
#T = 1/f
#Ts = 1/fs


#x = np.arange(fs)
#y = [ amp*np.sin(2*np.pi*f * (i/fs)) for i in x]



