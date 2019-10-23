from PIL import Image
import math
dimx = 800
dimy = 800

file = Image.new("RGB",(dimx,dimy))

file.putpixel((0,0),(255,0,0))


def circle(r,centx,centy):
	for i in range(360):
		x = centx +round(r*math.cos(math.radians(i)))
		y = centy +round(r*math.sin(math.radians(i)))
		file.putpixel((x,y),(255,0,0))

def line(x,y,l,c):
	for i in range(0,l):
		file.putpixel((x,y+i),(c,0,0))

def grad():
	for i in range(0,100):
		line(i,0,100,round(((255/10)*i)%255))

def rect(x1,y1,x2,y2,c):
	for i in range(0,abs(y1-y2)):
		for j in range(0,abs(x1-x2)):
			file.putpixel((x1+j,y1+i),(c,0,0))

def flip(c):
	if c == 255:
		return 0
	return 255

def checker(c):
	for y in range(0,800,100):
		for x in range(0,800,100):
			c = flip(c)
			rect(x, y, x+100, y+100, c)
		c = flip(c)
	  
checker(255)
file.save("demo_image.png","PNG")