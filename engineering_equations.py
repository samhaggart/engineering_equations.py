from math import sin, cos, radians, sqrt
import matplotlib.pyplot as plt
import numpy as np

def projectile(launch_angle, initial_velocity):
	while True:
		units = input("Are you using metric or standard units?")
		g = float()
		if "met" in units:
			g = -9.81
			break
		elif "sta" in units:
			g = -32.2
			break
	#Convert launch angle from degrees to radians for sin and cos function
	launch_angle = radians(launch_angle)
	#X and Y components of velocity at launch
	Vy = sin(launch_angle)*initial_velocity
	Vx = cos(launch_angle)*initial_velocity
	#Acceleration in metric units
	Ay = g
	Ax = 0
	#establishing coordinate system 0,0 at launch location
	Xi = 0
	Yi = 0
	#flight time
	tmax = abs((2 * Vy)/Ay)
		#create evenly spaced list of time from 0 to t
	timespan = np.linspace(0,tmax,50)
	
	#solve for x and y for each t in timespan and append to list
	x = Xi + Vx*timespan
	y = Yi + Vy*timespan + (.5*Ay*timespan**2)
	plt.plot(x,y)
	plt.ylabel("Height")
	plt.xlabel("Distance")
	plt.show()
	print("Flight time was ",tmax, "seconds.")



	





	