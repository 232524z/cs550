def zsquared(z):
	return [((z[0]**2)-(z[1]**2)),(2*z[0]*z[1])]

def zplusc(z,c):
	return [(z[0]+c[0]),(z[1]+c[1])]

def checkout(z):
	return 4 <= (z[0]**2)+(z[1]**2)

def mandelbrot(c, z =[0,0],i = 0):
	if checkout(z) == True:
		return i
	if i > 256:
		return 256
	z = zplusc(zsquared(z),c)
	return mandelbrot(c,z,i+1)
print(mandelbrot([1,1]))