import random
from point import point
from PIL import Image,ImageDraw
from progressbar import progressbar as bar

dimx=100
dimy=100
maze = Image.new("RGB",(dimx,dimy))

difficulty = 500
vlist = []
clist = []

def createv(diff,x,y,l):
	for i in range(diff):
		l.append(point(random.randint(0,x),random.randint(0,y)))

def connect(a,b,file):
	draw = ImageDraw.Draw(file)
	draw.line(((a.x,a.y),(b.x,a.y)),(255,0,0))
	draw.line(((b.x,a.y),(b.x,b.y)),(255,0,0))

def nearest(a,b):
	smallestD = 100000
	smallestI = [0,0]
	for i in range(len(a)):
		for j in range(len(b)):
			d = a[i].distance(b[j])
			if smallestD > d:
				smallestD = d
				smallestI = [i,j]
	return smallestI[1],[a[smallestI[0]],b[smallestI[1]]]

createv(difficulty,dimx,dimy,vlist)
maze.putpixel(vlist[0].tuple(),(0,255,0))
clist.append(vlist[0])
vlist.pop(0)

for i in bar(range(difficulty-1)):
	closest = nearest(clist,vlist)
	clist.append(closest[1][1])
	vlist.pop(closest[0])
	connect(closest[1][0],closest[1][1],maze)
maze.putpixel(clist[-1].tuple(),(0,255,0))
maze.save("maze.png","PNG")