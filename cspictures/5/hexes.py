import sys
from PIL import Image, ImageDraw
from numpy import interp
from progressbar import progressbar as bar
import math
from hslcolor import HSL

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



dimx, dimy = 1500, 1500
#makes the picture
file = Image.new("RGB",(dimx,dimy))
draw = ImageDraw.Draw(file)
#max number if iterations of the mandelbrot function
maxIt = 7
maxIto = maxIt
#sets the recursion limit so that maxIt will never hit it
sys.setrecursionlimit(1000)
while(maxIt>0):
	hexagon(550,400,400,5,(255,0,0))
	maxIt -= 1



file.save("hex.png","PNG")