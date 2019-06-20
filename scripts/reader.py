#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from std_msgs.msg import Float32

def callback(data):
    rospy.loginfo(rospy.get_caller_id() + " I heard %s", data.data)

def reader():

	rospy.init_node('reader', anonymous=True)

	rospy.Subscriber("convo",Float32, callback)
	
	rospy.spin()
	
if __name__== '__main__':
	reader()
