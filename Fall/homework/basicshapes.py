from numpy import interp
def circle(r,centx,centy):
	for i in range(360):
		x = centx +round(r*math.cos(math.radians(i)))
		y = centy +round(r*math.sin(math.radians(i)))
		file.putpixel((x,y),(255,0,0))

def line(x1,y1,x2,y2,c, file):
	if abs(x2-x1)>abs(y2-y1):
		slope = (y2-y1)/(x2-x1)
		for i in range(abs(x2-x1)):
			file.putpixel((x1+i,int(y1+slope*i)),c)
	else:
		slope = (x2-x1)/(y2-y1)
		for i in range(int(abs(y2-y1))):
			file.putpixel((int(x1+slope*i),y1+i),c)

def rect(x1,y1,x2,y2,c):
	for i in range(0,abs(y1-y2)):
		for j in range(0,abs(x1-x2)):
			file.putpixel((x1+j,y1+i),(c,0,0))