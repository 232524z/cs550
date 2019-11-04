#Ian
#OMH
#10/3/19
#This program draws three fractals. There is no randomness, so the same fractals should be drawn every time. 2 of the fractals are from the mandelbrot set, while the third is on that I created by drawing a hexagon, then drawing a smaller hexagon at the vertex of that hexagon, and continuing to draw hexagons for several iterations. I decided on the color schemes by trying many different things, and found that basic math, modulous, and trigonomoty make some very interesting color patterns.
#Sources: Spencer,
#required librarys: numpy. downloadable from pip (pip install numpy).
import sys
from PIL import Image, ImageDraw
from numpy import interp
import math
import colorsys
from progressbar import progressbar as bar

#converts HSL color to rgb color
def HSL(h,s,l):
	import colorsys
	color = [h, s, l]
	color = colorsys.hls_to_rgb(color[0]/360, color[1]/100, color[2]/100)
	color = [int(color[i]*255) for i in range(3)]
	return tuple(color)

#checks wether a given number is within the mandelbrot set
def mandelbrot(c,maxIt, z =complex(0,0),i = 0):
	if abs(z)>= 2 or i>=maxIt:
		return i
	return mandelbrot(c,maxIt,z**2 +c,i+1)

#Calculates what color a given pixel should be based on the value received from the mandelbrot function for that pixel
def mandelpixel1(x,y,dimx,dimy,xmin,xmax,ymin,ymax,maxIt,name):
	c = mandelbrot(complex(interp(x,[0,dimx],[xmin,xmax]),interp(y,[0,dimy],[ymin,ymax])),maxIt)
	r = 0
	g = 0
	b = (math.sin((c/500)*dimx*3.00))*255
	name.putpixel((x,y),(int(r),int(g),int(b)))

#does the same thing as the previous function, but with a different method for calculating the color
def mandelpixel2(x,y,dimx,dimy,xmin,xmax,ymin,ymax,maxIt,name):
	c = (256/maxIt)*(mandelbrot(complex(interp(x,[0,dimx],[xmin,xmax]),interp(y,[0,dimy],[ymin,ymax])),maxIt))
	r = math.cos(c*4)%256
	g = 0
	b = abs((c*4+50*math.cos(c)))%256
	name.putpixel((x,y),(int(r),int(g),int(b)))

#hexagon function, draws hexagons at each vertex of the previous hexagon until it reaches the max iterations
def hexagon(x,y,l,point, c,name,maxIt,maxIto,draw,count=0,):
	if count <= maxIt:
		for i in range(6):
			hexagon(x,y,l/2,point-1, c,name,maxIt,maxIto,draw, count+1)
			point = (point+1)%6
			angle = interp(point,[0,6],[0,2*math.pi])
			a,b = x,y
			x,y = x+l*math.cos(angle),y+l*math.sin(angle)
			if count == maxIt:
				draw.line((int(a),int(b), int(x),int(y)), fill=HSL(int((count/maxIto)*255),50,100))

#makes a mandelbrot fractal with given values
#REMOVE BAR!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
def runMandel(dimx,dimy,xmin,xmax,ymin,ymax,maxIt,name,type):
	savename = name
	name = Image.new("RGB",(dimx,dimy))
	sys.setrecursionlimit(maxIt+10)
	for i in bar(range(dimx)):
		for j in range(dimy):
			if type == 1:
				mandelpixel1(i,j,dimx,dimy,xmin,xmax,ymin,ymax,maxIt,name)
			else:
				mandelpixel2(i,j,dimx,dimy,xmin,xmax,ymin,ymax,maxIt,name)
	name.save(savename+".png", "PNG")

#makes a hexagon fractal with given values
def runHex(x,y,l,point,c,dimx,dimy,maxIt,name):
	savename = name
	maxIto = maxIt
	name = Image.new("RGB",(dimx,dimy))
	draw = ImageDraw.Draw(name)
	sys.setrecursionlimit(6**maxIt+4)
	while(maxIt>0):
		hexagon(x,y,l,point,c,name,maxIt,maxIto,draw)
		maxIt -= 1
	name.save(savename+".png","PNG")

#runs all of the functions with the values I chose to look good
# runMandel(1000, 1000,-.3158267837126886,-.315826561940633446,.6533639614499106,.6533641832219648,1000,"bluemandel", 1)
runMandel(1000, 1000,-.04268973253251546,-.042678548183545745, -.9899397662400176, -.9899285829010478,2000,"purplemandel", 2)
# runHex(550,400,400,5,(255,0,0),1500,1500,7, "hexpicture")