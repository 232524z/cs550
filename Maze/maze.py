import random
from point import point
from PIL import Image,ImageDraw
from progressbar import progressbar as bar

dimx=100
dimy=dimx
boarderWidth = 5
mazeDimx,mazeDimy=dimx-boarderWidth,dimy-boarderWidth
maze = Image.new("RGB",(dimx,dimy))

difficulty = dimx*15
vlist = []
clist = []

def createv(diff,w,x,y,l):
	for i in range(diff):
		l.append(point(random.randint(w,x),random.randint(w,y)))
		for j in l:
			while l[i].distance(j) < dimx/5:
				l.pop(-1)
				l.append(point(random.randint(w,x),random.randint(w,y)))


def connect(a,b,file):
	draw = ImageDraw.Draw(file)
	draw.line(((a.x,a.y),(b.x,a.y)),(255,255,255))
	draw.line(((b.x,a.y),(b.x,b.y)),(255,255,255))

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

def drawLines():
	for i in bar(range(difficulty-1)):
		closest = nearest(clist,vlist)
		clist.append(closest[1][1])
		vlist.pop(closest[0])
		connect(closest[1][0],closest[1][1],maze)

def choosePoints():
	l = [0,100000]
	for i in range(len(clist)):
		if clist[i].distance(point(0,0)) < l[1]:
			l = [i,clist[i].distance(point(0,0))]
	maze.putpixel(clist[l[0]].tuple(),(0,255,0))
	r = [0,100000]
	for i in range(len(clist)):
		if clist[i].distance(point(dimx,dimy)) < r[1]:
			r = [i,clist[i].distance(point(dimx,dimy))]
	maze.putpixel(clist[r[0]].tuple(),(0,255,0))

createv(difficulty,boarderWidth,mazeDimx,mazeDimy,vlist)
clist.append(vlist[0])
vlist.pop(0)

drawLines()
choosePoints()
maze.save("maze.png","PNG")