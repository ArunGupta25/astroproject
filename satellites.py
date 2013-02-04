import numpy
import galactic
import math
import pylab as p
import mpl_toolkits.mplot3d.axes3d as p3
from mayavi import mlab

ng_dtype = ([('name', str, 25),
				('ra', str, 25),
				('dec', str, 25),
				('eb-v', float),
				('(m-M)o', float),
				('(m-M)o err+', float),
				('(m-M)o err-', float),
				('vh(km/s)', float),
				('vh(km/s) err+', float),
				('vh(km/s) err-', float),
				('Vmag', float),
				('Vmag err+', float),
				('Vmag err-', float),
				('PA', float),
				('PA err+', float),
				('PA err-', float),
				('e=1-b/a', float),
				('e=1-b/a err+', float),
				('e=1-b/a err-', float),
				('muVo', float),
				('muVo err+', float),
				('muVo err-', float),
				('rh(arcmins)', float),
				('rh(arcmins) err+', float),
				('rh(arcmins) err-', float),
				('sigma_s(km/s)', float),
				('sigma_s(km/s) err+', float),
				('sigma_s(km/s) err-', float),
				('vrot_s(km/s)', float),
				('vrot_s(km/s) err+', float),
				('vrot_s(km/s) err-', float),
				('MHI', float),
				('sigma_g(km/s)', float),
				('sigma_g(km/s) err+', float),
				('sigma_g(km/s) err-', float),
				('vrot_g(km/s)', float),
				('vrot_g(km/s) err+', float),
				('vrot_g(km/s) err-', float),
				('[Fe/H]', float),
				('[Fe/H] err+', float),
				('[Fe/H] err-', float),
				('F', float),
				('references', str, 40)
				])

#master array of data
ngdata = numpy.loadtxt('nearbygalaxies1.dat', dtype=ng_dtype)

#initialize arrays for xyz coordinates and labels
xyz = numpy.empty((26,3))
names = []
fdistance = []

#populate the arrays with xyz coordinates
for i in range(0,26):

	#first transform each to galactic coordinates
	b = galactic.galactic(ngdata[i][1],ngdata[i][2])[0]
	bradians = b / 180 * math.pi
	l = galactic.galactic(ngdata[i][1],ngdata[i][2])[1]
	lradians = l / 180 * math.pi

	#calculate the distance to the object
	distance = math.pow(10, ((ngdata[i][4] + 5) / 5))

	fdistance.append(distance)

	help = distance * math.cos(bradians)

	y = help * math.sin(lradians)

	x = help * math.cos(lradians)

	z = distance * math.sin(bradians)

	xyz[i][0] = x
	xyz[i][1] = y
	xyz[i][2] = z

	#add in the object names
	#print ngdata[i][0]
	names.append(ngdata[i][0])

#break out the arrays
fname = names

fx = numpy.ravel(xyz[:,0])

fy = numpy.ravel(xyz[:,1])

fz = numpy.ravel(xyz[:,2])

fx[0] = 0
fy[0] = 0
fz[0] = 0

"""
#3d mayavi plot

s = mlab.points3d(fx[0], fy[0], fz[0], color=(0,1,1), mode='sphere', scale_factor=100)

for i in range(0,26):
	mlab.points3d(fx[i], fy[i], fz[i], color=(0,1,1), mode='sphere', scale_factor=5000, opacity=0.5)
	mlab.text3d(fx[i], fy[i], fz[i], fname[i], scale=5000)


axes = mlab.axes(s, extent = (-220000,220000, -220000,220000, -220000,220000), nb_labels=3)

mlab.title("satellites of the milky way galaxy", height=1, size=.5)
"""

#scatterplot of apparent magnitudes vs radius



fabsmag = []

for i in range(0,26):
	fdistance[i] = fdistance[i] / 1000
	fabsmag.append(ngdata[i][10] - ngdata[i][4])


fdistance.pop(0)
fabsmag.pop(0)

#p.scatter(fdistance, fabsmag)
#p.gca().invert_yaxis(); p.show()

#have to run this manually for some reason
for i in [0,1,2,3,7,9,10,11,12,14,15,16,17,18,19,20,22,23]:
	p.annotate(fname[i+1][0:3], xy=(fdistance[i], fabsmag[i]), xytext=(fdistance[i]+.1*fdistance[i], fabsmag[i] + .1*fabsmag[i]), arrowprops=dict(facecolor='black', shrink=0.1, width=1, frac=.01, headwidth=.1))

sat = [fname, fx, fy, fz, fabsmag]


