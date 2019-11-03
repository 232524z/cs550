#Ian
#OMH
#this program draws a representation of the madelbrot set
#sources: spencer, https://pypi.org/project/progressbar2/
import sys
from PIL import Image
from numpy import interp
from progressbar import progressbar as bar
def mandelbrot1(c, z =complex(0,0),i = 0):
	if abs(z)>= 2 or i>=maxIt:
		return i
	return mandelbrot1(c,z**2 +c,i+1)

#without numpy, ((xmax-xmin)/dimx)*x+xmin
def mandelpixel1(x,y):
	c = mandelbrot1(complex(interp(x,[0,dimx],[xmin,xmax]),interp(y,[0,dimy],[ymin,ymax])))
	r = 0
	g = 0
	b = ((c/500)*dimx*3.00)%256
	purplemandel.putpixel((x,y),(int(r),int(g),int(b)))


#dimensions of picture
dimx, dimy = 1000, 1000
#range of mandelbrot
xmin,xmax,ymin,ymax = -.3158267837126886,-.315826561940633446,.6533639614499106,.6533641832219648
#max number if iterations of the mandelbrot function
maxIt = 1000
#makes the picture
purplemandel = Image.new("RGB",(dimx,dimy))
#sets the recursion limit so that maxIt will never hit it
sys.setrecursionlimit(maxIt+4)
#this makes a progress bar count how far along it is in the for loop
#puts each pixel in place
for i in bar(range(dimx)):
	for j in range(dimy):
		mandelpixel1(i,j)
#saves the image
purplemandel.save("purplemandel.png","PNG")

def mandelbrot2(c, z =complex(0,0),i = 0):
	if abs(z)>= 2 or i>=maxIt:
		return i*(256/maxIt)
	return mandelbrot2(c,z**2 +c,i+1)

#without numpy, ((xmax-xmin)/dimx)*x+xmin
def mandelpixel2(x,y):
	c = mandelbrot2(complex(interp(x,[0,dimx],[xmin,xmax]),interp(y,[0,dimy],[ymin,ymax])))
	r = (c*4)%256
	g = 0
	b = (c*4)%256
	purplemandel.putpixel((x,y),(int(r),int(g),int(b)))


#dimensions of picture
dimx, dimy = 1000, 1000
#range of mandelbrot
xmin,xmax,ymin,ymax = -.04268973253251546,-.042678548183545745, -.9899397662400176, -.9899285829010478
#max number if iterations of the mandelbrot function
maxIt = 1000
#makes the picture
purplemandel = Image.new("RGB",(dimx,dimy))
#sets the recursion limit so that maxIt will never hit it
sys.setrecursionlimit(maxIt+4)
#this makes a progress bar count how far along it is in the for loop
#puts each pixel in place
for i in bar(range(dimx)):
	for j in range(dimy):
		mandelpixel2(i,j)
#saves the image
purplemandel.save("mpicture.png","PNG")