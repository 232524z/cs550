def mandelbrot(c, z =complex(0,0),i = 0):
	if abs(z)>= 2 or i>=256:
		return i
	return mandelbrot(c,z**2 +c,i+1)
print(mandelbrot(complex(1,1)))