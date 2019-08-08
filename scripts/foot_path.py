from numpy import *
from matplotlib.pyplot import *
import time
ion()

def update_plot(tnow,S,X,Y,U):
	#what S are we at now?
	Snow = tnow*U
	xnow = interp(Snow,S,X)
	ynow = interp(Snow,S,Y)
	line.set_data(xnow,ynow)
	


#create the sparse path. 
S = array([0,3,9,12,18])
X = array([2,2,8,8,2])
Y = array([25,22,22,25,25])

#linear speed (constant)
U = 3#inches per second
#what time are we at now?
tnow = 5

Snow,xnow,ynow = 0,0,0
# figure()
# plot(X,Y,'ro')
# axis('equal')
# xlabel('X (in)')
# ylabel('Y (in)')

fig = figure()
ax1 = fig.add_subplot(211)
ax2 = fig.add_subplot(212)
ax1.plot(S,X,'k')
ax2.plot(S,Y,'k')
show(block=False)
fig.canvas.draw()

#timestep (simulate time of your timed loop in ROS)
dt = 0.1

tnow = 0
Laps = 0

for k in range(0,1000):
	try:
		Smax = S[-1]#very last point in the S vector is the max
		#what is the time now?
		tnow = k*dt
		#what is the TOTAL distance traveled?
		Snow = tnow*U
		#how many laps have we done?
		Laps = floor(Snow/Smax)
		#where are we at on THIS lap?
		Srelative = Snow-Laps*Smax
		#now where should the foot be?
		xnow = interp(Srelative,S,X)
		ynow = interp(Srelative,S,Y)
		#now we plot those points
		ax1.clear()
		ax2.clear()
		ax1.plot(S,X,'k',Srelative,xnow,'ro')
		ax2.plot(S,Y,'k',Srelative,ynow,'ro')
		show(block=False)
		fig.canvas.draw()
		time.sleep(.01)



	except KeyboardInterrupt:
		close('all')
		break



