import numpy
import galactic
import math
import pylab as p
import mpl_toolkits.mplot3d.axes3d as p3
import thriidii

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

#populate the arrays with xyz coordinates
for i in range(0,26):

	#first transform each to galactic coordinates
	b = galactic.galactic(ngdata[i][1],ngdata[i][2])[0]
	bradians = b / 180 * math.pi
	l = galactic.galactic(ngdata[i][1],ngdata[i][2])[1]
	lradians = l / 180 * math.pi

	#calculate the distance to the object
	distance = math.pow(10, ((ngdata[i][4] + 5) / 5))

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

"""
#plot the xyz coordinates
fig = p.figure()
ax = p3.Axes3D(fig)
ax.plot_wireframe(x,y,z)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.scatter3D(numpy.ravel(xyz[:,0]), numpy.ravel(xyz[:,1]), numpy.ravel(xyz[:,2]), 'o', label='help')
p.show()
"""

#third party script to plot
thriidii.thriidii(0, 0, fx, fy, fz, fz, fname, 1,0.01, 0.5, 4, "X", "Y", "Z", 0, "green",1)