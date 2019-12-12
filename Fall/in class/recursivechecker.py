from PIL import Image
import math
dimx = 800
dimy = 800

file = Image.new("RGB",(dimx,dimy))
file.putpixel((0,0),(255,0,0))

def rect(x1,y1,x2,y2,c):
	for i in range(0,abs(y1-y2)):
		for j in range(0,abs(x1-x2)):
			file.putpixel((x1+j,y1+i),(c,0,0))



def checker(x1,y1,x2,y2):
	c = 255
	jsquare = True
	if (x2-x1) > 4 or (y2-y1) > 4:
		for y in range(y1,y2,round((y2-y1)/2)):
			for x in range(x1,x2,round((x2-x1)/2)):
				if jsquare:
					rect(x, y, x2, y2, c)
					jsquare = False
					if c == 255:
						c = 0
					else:
						c = 255
				else:
					checker(x,y,x2,y2)
checker(0, 0, 400, 400)










file.save("recursivechecker.png","PNG")