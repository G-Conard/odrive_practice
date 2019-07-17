#!/usr/bin/env python

# Author: Gabrielle Conard, July 2019
# File: ik_simulation.py
# This python script takes a given position of the foot (with respect to the hip)...
# ...and finds the angles of the upper and lower leg (femur and tibia) required to achieve that position.
# It then uses matplotlib to animate it.
# Based on Jake Vanderplas's script for a Double Pendulum simulator (see double_pendulum.py)

#basics
# import rospy
# roslib.load_manifest('odrive_ros')


import tf.transformations
import tf_conversions
import tf2_ros

# Imports message types and services from several libraries
# from std_msgs.msg import Float64Stamped, Int32Stamped
# from geometry_msgs.msg import TwistStamped, TransformStamped, PoseStamped
# import std_srvs.srv

import time
import traceback
# import Queue


from numpy import *
from matplotlib import pyplot as plt 
from matplotlib import animation


class InverseKinematics:
	def __init__(self, position = [-5, 18]):
		#if you need parameters, use the following
		#self.mything = rospy.get_param('param_name',default_value)

		# Publishers and Subscribers
		# Subscribe to a foot position P: (xP, yP)
		# self.sub = rospy.Subscriber("/footPositionX",PoseStamped,pos_callback)

		#publish leg angles (two separate publishers)
		#do I need to publish on a timer or only when I get a new value???
		# self.femur = rospy.Publisher("/theta_f", Float64Stamped, queue_size = 1)
		# self.tibia = rospy.Publisher("/theta_t",Float64Stamped, queue_size = 1)

		self.origin = (0,0)
		self.position = position


		# Class Variables

		# Measured Values:
		# All lengths are in inches and angles are in degrees
		self.length_f = 14.107
		self.length_t = 12.233
		self.theta_K_shift = 16.6
		self.theta_HKP_shift = 1.2
		self.theta_H = 16.9
		self.theta_t_shift = 15.8

		# To be calculated...
		self.d = None
		self.theta_P = None
		self.theta_K = None
		self.theta_HKP = None
		# Goal:
		self.theta_f = None
		self.theta_t = None





	def pos_callback(self):
		# Calculate distance from hip joint to foot (d)...
		# ...and angle with respect to x-axis
		self.d = sqrt(self.position[0]**2 + self.position[1]**2)
		print(self.d)
		self.theta_P = arctan(self.position[1] / self.position[0])

		# Compute angles foot-hip-knee (theta_K) and hip-knee-foot (theta_HKP)
		print((self.length_f**2 + self.d**2 - self.length_t**2)/(2 * self.d * self.length_f))
		self.theta_K = arccos((self.length_f**2 + self.d**2 - self.length_t**2)/(2 * self.d * self.length_f))
		print((self.length_t**2 + self.length_f**2 - self.d**2) / (2 * self.length_f * self.length_t))
		self.theta_HKP = arccos((self.length_t**2 + self.length_f**2 - self.d**2) / (2 * self.length_f * self.length_t))

		# Calculate desired angles of femur and tibia (including offsets)...
		# ...and publish results
		# self.theta_f = Float64Stamped()
		# self.theta_f.header.stamp = rospy.Time.now()
		# self.theta_f = self.theta_P - self.theta_K - self.theta_K_shift + self.theta_H
		# self.femur.publish(theta_f)

		# self.theta_t = Float64Stamped()
		# self.theta_t.header.stamp = rospy.Time.now()
		# self.theta_t = self.theta_HKP - self.theta_HKP_shift - self.theta_t_shift
		# self.tibia.publish(theta_t)

		self.theta_f = self.theta_K
		print(self.theta_f * (180/pi))
		self.theta_t = self.theta_HKP
		print(self.theta_t * (180/pi))

		x = cumsum([self.origin[0],
			self.length_f * cos(self.theta_f),
			self.length_t * cos(self.theta_f + ((2 * pi) - abs(self.theta_t)))])
		print(cos(self.theta_f + ((2 * pi) - self.theta_t)))
		y = cumsum([self.origin[1],
			self.length_f * sin(self.theta_f),
			self.length_t * sin(self.theta_f + ((2 * pi) - abs(self.theta_t)))])

		print("x:" + str(x))
		print("y:" + str(y))
		return (x,y)


leg = InverseKinematics([5, 18])


fig = plt.figure()
ax = fig.add_subplot(111, aspect='equal', autoscale_on=False,
                     xlim=(-30, 30), ylim=(-30, 30))

plt.gca().invert_yaxis()
ax.grid()

line, = ax.plot([], [], 'o-', lw = 2)

line.set_data(leg.pos_callback())



plt.show()
