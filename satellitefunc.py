import numpy
import galactic
import math
import pylab as p
import mpl_toolkits.mplot3d.axes3d as p3
from mayavi import mlab

def mayaplot(xyznamearray):

	x = xyznamearray[1]
	y = xyznamearray[2]
	z = xyznamearray[3]
	labels = xyznamearray[0]

	s = mlab.points3d(x[0], y[0], z[0], color=(0,1,1), mode='sphere', scale_factor=100)

	for i in range(0,26):
		mlab.points3d(x[i], y[i], z[i], color=(0,1,1), mode='sphere', scale_factor=5000, opacity=0.5)
		mlab.text3d(x[i], y[i], z[i], labels[i], scale=5000)


	axes = mlab.axes(s, extent = (-220000,220000, -220000,220000, -220000,220000), nb_labels=3)

#give angle in radians
def rotatez(angle, xyznamearray):

	x = xyznamearray[1]
	y = xyznamearray[2]
	z = xyznamearray[3]
	labels = xyznamearray[0]

	for i in range(0,26):
		x[i] = x[i]*math.cos(angle) - y[i]*math.sin(angle)
		y[i] = x[i]*math.sin(angle) + y[i]*math.cos(angle)
		z[i] = z[i]

	return [labels, x, y, z]

def rotatex(angle, xyznamearray):

	x = xyznamearray[1]
	y = xyznamearray[2]
	z = xyznamearray[3]
	labels = xyznamearray[0]

	for i in range(0,26):
		y[i] = y[i]*math.cos(angle) - z[i]*math.sin(angle)
		z[i] = y[i]*math.sin(angle) + z[i]*math.cos(angle)
		x[i] = x[i]

	return [labels, x, y, z]

def rotatey(angle, xyznamearray):

	x = xyznamearray[1]
	y = xyznamearray[2]
	z = xyznamearray[3]
	labels = xyznamearray[0]

	for i in range(0,26):
		z[i] = z[i]*math.cos(angle) - x[i]*math.sin(angle)
		x[i] = z[i]*math.sin(angle) + x[i]*math.cos(angle)
		y[i] = y[i]

	return [labels, x, y, z]

#uses 20 Mpc along the -x axis
def findtheta(sat):

	labels = sat[0]
	absmagvalues = sat[4]

	#find the distance to each point from 20*10**6,0,0
	distance = []
	bvalues = []
	lvalues = []
	for i in range(0,26):
		dval = ((sat[1][i]-20000000)**2 + (sat[2][i]-0)**2 + (sat[3][i]-0)**2)**0.5
		distance.append(dval)

		newx = sat[1][i] - 20000000
		newy = sat[2][i]
		newz = sat[3][i]

		#b in radians
		b = math.asin(newz/dval)
		bvalues.append(b)

		#l in radians
		l = math.acos(newx / (dval * math.cos(b)))
		lvalues.append(l)

	#find the ra and dec with the new coordinate scheme at 20 Mpc out on the +x axis
	ravalues = []
	decvalues = []
	for i in range(0,26):
		dec = math.asin(math.cos(bvalues[i])*math.cos(0.478220215)*math.sin(lvalues[i]-0.575958653)+math.sin(bvalues[i])*math.sin(0.478220215))
		#to degrees
		decdegs = dec * 180 / math.pi

		decvalues.append(decdegs)

		y = math.cos(bvalues[i])*math.cos(lvalues[i]-0.575958653)
		x = math.sin(bvalues[i])*math.cos(0.478220215) - math.cos(bvalues[i])*math.sin(0.478220215)*math.sin(lvalues[i]-0.575958653)

		ra = math.atan(y/x)
		#to degrees
		radegs = ra * 180 / math.pi
		#put it in the correct quadrant
		radegs = radegs + 180
		radegs = (radegs + 192.25) / 15

		ravalues.append(radegs)

	#calculate the angular distance
	angdistvalues = []
	for i in range(0,26):
		dec1 = decvalues[0] * math.pi / 180
		dec2 = decvalues[i] * math.pi / 180
		ra1 = ravalues[0] * math.pi / 180
		ra2 = ravalues[i] * math.pi / 180
		angdist = math.sin(dec1)*math.sin(dec2) + math.cos(dec1)*math.cos(dec2)*math.cos(ra1-ra2)
		#convert from radians to arcminutes
		angdist = angdist * 3437.74677
		angdistvalues.append(angdist)

	#calculate the distance modulus and apparent magnitude
	distmodvalues = []
	appmagvalues = []
	for i in range(0,26):
		distmod = 5*math.log10(distance[i]) - 5
		distmodvalues.append(distmod)

		appmag = absmagvalues[i] + distmod
		appmagvalues.append(appmag)

	return [labels, absmagvalues, distance, angdistvalues, appmagvalues]

#give a lower bound for apparent mag and list of satellites
def absmagplot(lbound, thetalist):
	for i in range(1,26):
		if thetalist[4][i] > lbound:
			p.scatter(thetalist[3][i], thetalist[1][i])
			p.annotate(thetalist[0][i], xy=(thetalist[3][i], thetalist[1][i]), xytext=(1.2*thetalist[3][i], 1.2*thetalist[1][i]))

	p.gca().invert_yaxis(); p.show()





