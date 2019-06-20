#!/usr/bin/env python

import rospy
from std_msgs.msg import String
from std_msgs.msg import Float32

def counter():
	#pub = rospy.Publisher('convo', String, queue_size=10)
	pub = rospy.Publisher('convo', Float32, queue_size=10)
	rospy.init_node('counter', anonymous=True)
	rate = rospy.Rate(1)
	
	x = 1
	while not rospy.is_shutdown():
		#count_string = "%s" % x		
		#rospy.loginfo(count_string)
		#pub.publish(count_string)
			
		rospy.loginfo(x)
		pub.publish(x)

		x = x + 1
		rate.sleep()

if __name__ == '__main__':
	try:
		counter()
	except rospy.ROSInterruptException:
		pass


