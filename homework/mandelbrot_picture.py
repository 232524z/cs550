#Ian
#OMH
#this program draws a representation of the madelbrot set
#sources: spencer, https://pypi.org/project/progressbar2/
import sys
from PIL import Image
from numpy import interp
import progressbar
dimx = 1000
dimy = 1000
maxIt = 10000
file = Image.new("RGB",(dimx,dimy))
def mandelbrot(c, z =complex(0,0),i = 0):
	if abs(z)>= 2 or i>=maxIt:
		return i*(256/maxIt)
	return mandelbrot(c,z**2 +c,i+1)
def mandelpixel(x,y):
	c =200/mandelbrot(complex(interp(x,[0,dimx],[-2,2]),interp(y,[0,dimy],[-2,2])))
	file.putpixel((x,y),(int(c),0,0))

sys.setrecursionlimit(maxIt+4)
#this makes a progress bar count how far along it is in the for loop
for i in progressbar.progressbar(range(dimx)):
	for j in range(dimy):
		mandelpixel(i,j)

file.save("mpicture.png","PNG")