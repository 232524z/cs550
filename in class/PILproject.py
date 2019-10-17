from PIL import Image
import math
dimx = 100
dimy = 100

file = Image.new("RGB",(dimx,dimy))

def circle(r,centx,centy):
	for i in range(360):
		x = centx +round(r*math.cos(math.radians(i)))
		y = centy +round(r*math.sin(math.radians(i)))
		file.putpixel((x,y),(255,0,0))

def rect(x1,y1,x2,y2,c):
	for i in range(0,abs(y1-y2)):
		for j in range(0,abs(x1-x2)):
			file.putpixel((x1+j,y1+i),(c,0,0))
for i in range(0, 50, 5):
	circle(i,50,50)
file.save("demo_image.png","PNG")