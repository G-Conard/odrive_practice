#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from std_msgs.msg import Float32
import numpy as np

def callback(x):
    rospy.loginfo(rospy.get_caller_id() + " I heard %s", x.data)
    y = np.sqrt(15000**2-np.power(x.data, 2))
    ymsg = Float32()
    ymsg.data = y
    pub.publish(ymsg)
    rospy.loginfo(y)

def seeWave():

	rospy.init_node('seeWave', anonymous=True)

	rospy.Subscriber("sineWave",Float32, callback)
	
	rospy.spin()
	
if __name__== '__main__':
	pub = rospy.Publisher("seeWave", Float32, queue_size = 1)
	seeWave()
