import sys
from PIL import Image, ImageDraw
from numpy import interp
from progressbar import progressbar as bar
import math
import colorsys

def HSL(h,s,l):
	import colorsys
	color = [h, s, l]
	color = colorsys.hls_to_rgb(color[0]/360, color[1]/100, color[2]/100)
	color = [int(color[i]*255) for i in range(3)]
	return tuple(color)

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
	bluemandel.putpixel((x,y),(int(r),int(g),int(b)))

#without numpy, ((xmax-xmin)/dimx)*x+xmin
def mandelpixel2(x,y):
	c = mandelbrot2(complex(interp(x,[0,dimx],[xmin,xmax]),interp(y,[0,dimy],[ymin,ymax])))
	r = (c*4)%256
	g = 0
	b = (c*4)%256
	purplemandel.putpixel((x,y),(int(r),int(g),int(b)))

def hexagon(x,y,l,point, c, count=0):
	if count <= maxIt:
		for i in range(6):
			hexagon(x,y,l/2,point-1, c, count+1)
			point = (point+1)%6
			angle = interp(point,[0,6],[0,2*math.pi])
			a,b = x,y
			x,y = x+l*math.cos(angle),y+l*math.sin(angle)
			if count == maxIt:
				draw.line((int(a),int(b), int(x),int(y)), fill=HSL(int((count/maxIto)*255),50,100))

def mandelbrot2(c, z =complex(0,0),i = 0):
	if abs(z)>= 2 or i>=maxIt:
		return i*(256/maxIt)
	return mandelbrot2(c,z**2 +c,i+1)


#dimensions of picture
dimx, dimy = 1000, 1000
#range of mandelbrot
xmin,xmax,ymin,ymax = -.3158267837126886,-.315826561940633446,.6533639614499106,.6533641832219648
#max number if iterations of the mandelbrot function
maxIt = 1000
#makes the picture
bluemandel = Image.new("RGB",(dimx,dimy))
#sets the recursion limit so that maxIt will never hit it
sys.setrecursionlimit(maxIt+4)
#this makes a progress bar count how far along it is in the for loop
#puts each pixel in place
for i in bar(range(dimx)):
	for j in range(dimy):
		mandelpixel1(i,j)
#saves the image
bluemandel.save("bluemandel.png","PNG")



dimx, dimy = 1500, 1500
#makes the picture
hexpicture = Image.new("RGB",(dimx,dimy))
draw = ImageDraw.Draw(hexpicture)
#max number if iterations of the mandelbrot function
maxIt = 7
maxIto = maxIt
#sets the recursion limit so that maxIt will never hit it
sys.setrecursionlimit(1000)
while(maxIt>0):
	hexagon(550,400,400,5,(255,0,0))
	maxIt -= 1
hexpicture.save("hex.png","PNG")


#dimensions of picture
dimx, dimy = 1000, 1000
#range of mandelbrot
xmin,xmax,ymin,ymax = -.04268973253251546,-.042678548183545745, -.9899397662400176, -.9899285829010478
#max number if iterations of the mandelbrot function
maxIt = 2000
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
purplemandel.save("purplemandel.png","PNG")