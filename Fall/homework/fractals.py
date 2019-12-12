#Ian
#OMH
#11/4/19
#This program draws three fractals. There is no randomness, so the same fractals should be drawn every time. 2 of the fractals are from the mandelbrot set, while the third is on that I created by drawing a hexagon, then drawing a smaller hexagon at the vertex of that hexagon, and continuing to draw hexagons for several iterations. I decided on the color schemes by trying many different things, and found that basic math, modulous, and trigonomoty make some very interesting color patterns for the mandelbrot images. For the hexagon fractal, the colors are on an HSL slider, with the largest hexagons being closest to 0, and the smallest closest to 360. I really like the effect this gives, since each layer of hexagons is a similar color to its neighbors, but the overall difference is enough that each hexagon is distinct.
#Sources: Spencer, http://atopon.org/mandel/,https://docs.python.org/3.6/library/colorsys.html
#required librarys: numpy. downloadable from pip (pip install numpy).
import sys
from PIL import Image, ImageDraw
from numpy import interp
import math
import colorsys

#converts HSL color to rgb color
def HSL(h,s,l):
	color = [h, s, l]
	color = colorsys.hls_to_rgb(color[0]/360, color[1]/100, color[2]/100)
	color = [int(color[i]*255) for i in range(3)]
	return tuple(color)

#checks whether a given number is within the mandelbrot set
def mandelbrot(c,maxIt, z =complex(0,0),i = 0):
	if abs(z)>= 2 or i>=maxIt:
		return i
	return mandelbrot(c,maxIt,z**2 +c,i+1)

#Calculates what color a given pixel should be based on the value received from the mandelbrot function for that pixel
def mandelpixel1(x,y,dimx,dimy,xmin,xmax,ymin,ymax,maxIt,name):
	#C is simply the value given by the mandelbrot dunction for the coordinates.
	c = mandelbrot(complex(interp(x,[0,dimx],[xmin,xmax]),interp(y,[0,dimy],[ymin,ymax])),maxIt)
	r = 40*(1+math.sin(c))
	g = 0
	b = (math.sin((c/500)*dimx*3.00))*255
	name.putpixel((x,y),(int(r),int(g),int(b)))

#does the same thing as the previous function, but with a different method for calculating the color
def mandelpixel2(x,y,dimx,dimy,xmin,xmax,ymin,ymax,maxIt,name):
	#C is simply the value given by the mandelbrot dunction for the coordinates.
	c = (256/maxIt)*(mandelbrot(complex(interp(x,[0,dimx],[xmin,xmax]),interp(y,[0,dimy],[ymin,ymax])),maxIt))
	r = math.cos(c*4)%256
	g = 0
	b = abs((c*4+50*math.cos(c)))%256
	name.putpixel((x,y),(int(r),int(g),int(b)))

#hexagon function, draws hexagons at each vertex of the previous hexagon until it reaches the max iterations
def hexagon(x,y,l,point, c,name,maxIt,maxIto,draw,count=0,):
	if count <= maxIt:
		for i in range(6):
			#draws another hexagon at each vertex
			hexagon(x,y,l/2,point-1, c,name,maxIt,maxIto,draw, count+1)
			#changes the vertex by 1
			point = (point+1)%6
			#converts wich vertex it is to an angle
			angle = interp(point,[0,6],[0,2*math.pi])
			#sets a,b to x,y, then changes x,y, so that each line is drawn from the previous position to the new position
			a,b = x,y
			x,y = x+l*math.cos(angle),y+l*math.sin(angle)
			#only draws the hexagon if it is the smallest in the max iterations
			if count == maxIt:
				draw.line((int(a),int(b), int(x),int(y)), fill=HSL(int((count/maxIto)*255),50,100))

#makes a mandelbrot fractal with given values
def runMandel(dimx,dimy,xmin,xmax,ymin,ymax,maxIt,name,type):
	#stores the original name so that it can save the file, than creates an image name
	savename = name
	name = Image.new("RGB",(dimx,dimy))
	#sets the recursion limit above maxIt so that the maximum recursion depth will never be reached
	sys.setrecursionlimit(maxIt+10)
	#runs through every pixel, calulates the the color, and sets each pixel to that color
	for i in (range(dimx)):
		for j in range(dimy):
			#this chooses wether to run mandelpixel1 or mandelpixel 2 based in which design was chosen. It allows both fractals to be drawn using the same function.
			if type == 1:
				mandelpixel1(i,j,dimx,dimy,xmin,xmax,ymin,ymax,maxIt,name)
			else:
				mandelpixel2(i,j,dimx,dimy,xmin,xmax,ymin,ymax,maxIt,name)
	#saves the picture using the provided name
	name.save(savename+".png", "PNG")

#makes a hexagon fractal with given valuesx
#Note: this function uses recursion, and unfortunaly must calculate some of the same values multiple times. To make this program faster, I changed it so that it would save the values it calculated and use them later, rather than recalculate them. This turned out to be signifacantly slower. Although in theory it is possible to increase the speed by eliminating repeat calculations, in practice it did not appear to be feasible.
def runHex(x,y,l,point,c,dimx,dimy,maxIt,name):
	#stores the original name so that it can save the file, than creates an image name
	savename = name
	#maxIto is the original maxIt value. maxIt changes as the function is executed, but the orininal maxIt value is still needed for calculating the colors of the hexagons
	maxIto = maxIt
	name = Image.new("RGB",(dimx,dimy))
	#this gives the ability to use the built in draw function
	draw = ImageDraw.Draw(name)
	#the total number of recursions is 6^max iterations, so the recurion limit needs to be higher
	sys.setrecursionlimit(6**maxIt+4)
	#runs through th hexagon program, draws the smallest hexagon, then repeats with the second smallest, third smallest, etc
	while(maxIt>0):
		hexagon(x,y,l,point,c,name,maxIt,maxIto,draw)
		maxIt -= 1
	#saves the picture using the provided name
	name.save(savename+".png","PNG")

#runs all of the functions with the values I chose to look good
#makes the dark blue and red mandelbrot function (mandelpixel1)
runMandel(1000, 1000,-.3158267837126886,-.315826561940633446,.6533639614499106,.6533641832219648,1000,"bluemandel", 1)
#makes the purple/blue/red mandelbrot fractal (mandelpixel2)
runMandel(1000, 1000,-.04268973253251546,-.042678548183545745, -.9899397662400176, -.9899285829010478,2000,"purplemandel", 2)
#makes the hexagon fractal
runHex(367,267,267,5,(255,0,0),1000,1000,7, "hexpicture")

#The values above have been selected based on comments from many different people. People seemed to like fractals that were not monochromatic. I originally had only 1 color per fractal, only varying the shades. I feel that the splashes of color really improved the fractals. When I first made the hexagon function, the largest hexagons drew first, then the second largest, and so on. Spencer commented that it would look much more interesting if the largest hexagons were drawn on top, and the smallest on the bottom. I changed the hexagon function so that it worked this way, and I am very happy with the results.