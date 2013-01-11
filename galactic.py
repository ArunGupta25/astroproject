import math

#book example
#alpha in radians = 155.250 degrees
#ra = 2.70962366
#delta in radian = 10.053056 degrees
#dec = 0.175458927

"""
#canis major
radeg = 108.1455
decdeg = 27.6667
ra = radeg * math.pi / 180
dec = decdeg * math.pi / 180
"""

def galactic(rastr, decstr):

	rahours = float(rastr[0:rastr.index(':')])
	newrastr = rastr[rastr.index(':')+1:]
	ramins = float(newrastr[0:newrastr.index(':')])
	rasecs = float(newrastr[newrastr.index(':')+1:])

	#convert minutes and seconds to hours
	raminshours = ramins / 60.0
	rasecshours = rasecs / 3600.0
	#convert hours to degrees
	radegs = (rahours + raminshours + rasecshours) / 24.0 * 360
	#in radians
	ra = radegs / 180 * math.pi

	#break apart the string
	decdeg = float(decstr[0:decstr.index(':')])
	newdecstr = decstr[decstr.index(':')+1:]
	decmins = float(newdecstr[0:newdecstr.index(':')])
	decsecs = float(newdecstr[newdecstr.index(':')+1:])

	decminsdeg = decmins / 60
	decsecsdeg = decsecs / 3600

	#total degrees
	decdegs = decdeg + decminsdeg + decsecsdeg
	#in radians
	dec = decdegs / 180 * math.pi


	#galactic latitude in radians
	bradians = math.asin( math.cos(dec) * math.cos(0.478220215) * math.cos(ra - 3.35539549) + math.sin(dec) * math.sin(0.478220215))
	#in degrees
	b = bradians / math.pi * 180

	#galactic longitude in radians
	l = math.atan( (math.sin(dec) - math.sin(bradians) * math.sin(0.478220215)) / (math.cos(dec) * math.sin(ra - 3.35539549) * math.cos(0.478220215))) 

	#+ 0.575958653
	#in degrees
	l = l / math.pi * 180

	x = (math.sin(dec) - math.sin(bradians) * math.sin(0.478220215))
	y = (math.cos(dec) * math.sin(ra - 3.35539549) * math.cos(0.478220215))

	if x < 0 and y >0 and l < 0:
		l = l + 180

	if x > 0 and y < 0 and l < 0:
		l = l + 360

	if x < 0 and y < 0:
		l = l+180

	l = l + 33

	if l > 360:
		l = l - 360



	bl = []
	bl.append(b)
	bl.append(l)

	#returns an array of b and l in degrees
	#print bl
	return bl

#print ngdata[1]