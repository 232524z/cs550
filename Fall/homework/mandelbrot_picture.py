#Ian
#OMH
#this program draws a representation of the madelbrot set
#sources: spencer, https://pypi.org/project/progressbar2/, https://stackoverflow.com/questions/32673359/systemerror-new-style-getargs-format-but-argument-is-not-a-tuple
import sys
from PIL import Image
from numpy import interp
from progressbar import progressbar as bar
from hslcolor import HSL
def mandelbrot(c, z =complex(0,0),i = 0):
	if abs(z)>= 2 or i>=maxIt:
		return i*(256/maxIt)
	return mandelbrot(c,z**2 +c,i+1)

#without numpy, ((xmax-xmin)/dimx)*x+xmin
def mandelpixel(x,y):
	c = mandelbrot(complex(interp(x,[0,dimx],[xmin,xmax]),interp(y,[0,dimy],[ymin,ymax])))
	file.putpixel((x,y),HSL(270-60*(c/maxIt),70+30*(c/maxIt),100-90*(c/maxIt)))






#dimensions of picture
dimx, dimy = 500, 500
#makes the picture
file = Image.new("RGB",(dimx,dimy))
#max number if iterations of the mandelbrot function
maxIt = 2000
#sets the recursion limit so that maxIt will never hit it
sys.setrecursionlimit(maxIt+4)



#range of mandelbrot
xmin,xmax,ymin,ymax = -2,2, -2, 2



# this makes a progress bar count how far along it is in the for loop
# puts each pixel in place
for i in bar(range(dimx)):
	for j in range(dimy):
		mandelpixel(i,j)
#saves the image


