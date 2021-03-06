#Ian
#OMH
#this program draws a representation of the madelbrot set
#sources: spencer, https://pypi.org/project/progressbar2/
import sys
from PIL import Image
from numpy import interp
from progressbar import progressbar as bar
def mandelbrot(c, z =complex(0,0),i = 0):
	if abs(z)>= 2 or i>=maxIt:
		return i*(256/maxIt)
	return mandelbrot(c,z**2 +c,i+1)

#without numpy, ((xmax-xmin)/dimx)*x+xmin
def mandelpixel(x,y):
	c = mandelbrot(complex(interp(x,[0,dimx],[xmin,xmax]),interp(y,[0,dimy],[ymin,ymax])))
	r = (c*2)%256
	g = 0
	b = (c*2)%256
	file.putpixel((x,y),(int(r),int(g),int(b)))


#dimensions of picture
dimx, dimy = 1000, 1000
#range of mandelbrot
xmin,xmax,ymin,ymax = -.1673739482624005,-.16737350864965467,-1.04136478102112,-1.0413643414083742
#max number if iterations of the mandelbrot function
maxIt = 2000
#makes the picture
file = Image.new("RGB",(dimx,dimy))
#sets the recursion limit so that maxIt will never hit it
sys.setrecursionlimit(maxIt+4)
#this makes a progress bar count how far along it is in the for loop
#puts each pixel in place
for i in bar(range(dimx)):
	for j in range(dimy):
		mandelpixel(i,j)
#saves the image
file.save("mpicture.png","PNG")