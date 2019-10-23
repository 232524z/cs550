#Ian
#OMH
#10/23/19
#This program makes concentric red circles on the screen at random locations, that fade into the black background. I wanted to have different colored circles, but I was having difficulty converting from HSB color mode to RGB, so I could not accomplish it. I think it still has a very pleasing effect.
#Sources: none
from PIL import Image
import math
import random
from os import system
dimx = 1000
dimy = 1000
file = Image.new("RGB",(dimx,dimy))
def circle(r,centx,centy, c):
	for i in range(int(360)*4):
		x = centx +round(r*math.cos(math.radians(int(i/4))))
		y = centy +round(r*math.sin(math.radians(int(i/4))))
		try:
			file.putpixel((x,y),(c,0,0))
		except:
			pass

def glow(x,y):
	c = random.randint(0,255)
	for i in range(0, 100, 5):
		circle(i,x,y,((255-5*i)))

for i in range(500):
	glow(random.randint(0,dimx),random.randint(0,dimy))
	_ = system("clear")
	print((i/5),"%")


file.save("reddrawing.png","PNG")