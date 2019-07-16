#!/usr/bin/env python

#basics
import rospy
roslib.load_manifest('odrive_practice')

#load all the message types you need to publish or subscribe to
from std_msgs.msg import String
from std_msgs.msg import Float32Stamped

#import any relevant python packages for you (numpy, opencv, etc.)
import numpy as np



class PubSub:
	def __init__(self):

		#if you need parameters, use the following
		#self.mything = rospy.get_param('param_name',default_value)

		#now set up any subscribers
		self.sub = rospy.Subscriber("/subtopic",Float32Stamped,self.pubcallback)
		#what class-owned variables do i want from this topic?
		self.subbed_val = None

		#now set up your publisher
		
		#this publisher will only publish when we get a new value
		self.pubslow = rospy.Publisher("/pubslow",Float32Stamped,queue_size=1)

		#this publisher will publish on a timer.
		self.pubfast = rospy.Publisher("/pubfast",Float32Stamped,queue_size=1)

		#now set up a timed loop
		rospy.Timer(rospy.Duration(0.01),self.timercallback,oneshot=False)


	def pubcallback(self,data):
		#right now, this time is LOCAL. I can't access it from another function in the class.
		time_this_happened = data.header.stamp
		self.subbed_val = data.data

		output = Float32Stamped()
		output.header.stamp = rospy.Time.now()
		output.data = self.subbed_val*2.
		self.pubslow.publish(output)

	def timercallback(self,data):
		#now we will use the class-owned variable we subscribed to to publish a fast topic
		output =Float32Stamped()
		output.header.stamp = rospy.Time.now()
		output.data = self.subbed_val*3.
		self.pubfast.publish(output)

def main(args):
	rospy.init_node('pubsub',anonymous=True)
	PS = PubSub()

	try:
		rospy.spin()
	except KeyboardInterrupt:
		print "shutting down"

if __name__=='__main__':
	main(sys.argv)
