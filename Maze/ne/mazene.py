import random
from pointne import point
from PIL import Image,ImageDraw
from progressbar import progressbar as bar

dimx,dimy=100,100
boarderWidth = 1
mazeDimx,mazeDimy=dimx-boarderWidth*2,dimy-boarderWidth*2
maze = Image.new("RGB",(dimx,dimy))

difficulty = 500
vlist = []
clist = []

def createv(diff,w,x,y,l):
	for i in range(diff):
		l.append(point(random.randint(w,x),random.randint(w,y),random.randint(0,100)))
		for j in l:
			while l[i].distance(j) < dimx/25:
				l.pop(-1)
				l.append(point(random.randint(w,x),random.randint(w,y),random.randint(0,100)))


def connect(a,b,file):
	draw = ImageDraw.Draw(file)
	draw.line(((a.x,a.y),(b.x,a.y)),(255,0,0))
	draw.line(((b.x,a.y),(b.x,b.y)),(255,0,0))

def nearest(a,b):
	smallestD = 100000
	smallestI = [0,0]
	lowest = 10000
	ind = 0
	for i in range(len(b)):
		if lowest > b[i].weight:
			lowest = b[i].weight
			ind = i
	for i in range(len(a)):
		d = a[i].distance(b[ind])
		if smallestD > d:
			smallestD = d
			smallestI = [i,ind]
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

maze.save("mazene.png","PNG")