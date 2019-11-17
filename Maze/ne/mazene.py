#Ian
#11/18/19
#Sources:Spencer, https://www.tutorialspoint.com/python3/python_dictionary.htm

import random
from pointne import point
from PIL import Image, ImageDraw
from progressbar import progressbar as bar

def createv():
	global vertexlist
	#creates vertices for every point on the grid, including gutters
	vertexlist=[[point(x,y) for y in range(gridy+2)] for x in range(gridx+2)]

	#makes the gutters be counted so they don't interfere later
	for i in range(gridx):
		vertexlist[0][i].counted = True
		vertexlist[gridy-1][i].counted = True
		vertexlist[0][i].gutter = True
		vertexlist[gridy-1][i].gutter = True
	for i in range(gridy):
		vertexlist[i][0].counted = True
		vertexlist[i][gridx-1].counted = True
		vertexlist[i][0].gutter = True
		vertexlist[i][gridx-1].gutter = True

def createE():
	global edgedic
	for i in range(gridx):
		for j in range(gridy):
			#for every edge, generates a random weight and adds it to a dictionary. The coordinates of the start point followed by the endpoint is the key.
			edgedic[((i,j),(i+1,j))]=random.random()
			edgedic[((i,j),(i,j+1))]=random.random()

def lowest1(x,y):
	#list for the potential edges to reveal
	l = []

	#if the points above, below, to the left, and right are not yet counted, adds the connecting edges
	if vertexlist[x+1][y].counted == False:
		l.append(((x,y),(x+1,y)))
	if vertexlist[x-1][y].counted == False:
		l.append(((x,y),(x-1,y)))
	if vertexlist[x][y+1].counted == False:
		l.append(((x,y),(x,y+1)))
	if vertexlist[x][y-1].counted == False:
		l.append(((x,y),(x,y-1)))
	#s is the best contendor for the lowest value. The first number is the index in the list l, the second number is the weight of the edge.
	s = [0,1000]
	for i in range(len(l)):
		w = 0
		try:
			w = edgedic[l[i]]
		except:
			pass
		if w< s[1]:
			s = [i,w]
	#if there is a lowest value, returns the edge, and its weight
	if s != [0,1000]:
		return l[s[0]],s[1]
	return None




def lowestAll():
	global vertexlist
	counted = []
	for i in range(len(vertexlist)):
		for j in range(len(vertexlist[i])):
			if vertexlist[i][j].counted and vertexlist[i][j].gutter == False:
				counted.append(vertexlist[i][j])
	s = [0,1000]
	for i in range(len(counted)):
		try:
			w = lowest1(counted[i].x,counted[i].y)
			if w[1]< s[1]:
				s = w
		except:
			pass
	if s != [0,1000]:
		a,b = s[0][1][0],s[0][1][1]
		x,y = s[0][0][0],s[0][0][1]
		draw.line(((x*2,y*2),(a*2,b*2)),(255,255,255))
		vertexlist[a][b].counted = True


gridx,gridy = 20,20
dimx,dimy=gridx*2-1,gridy*2-1
maze = Image.new("RGB",(dimx,dimy))
draw = ImageDraw.Draw(maze)
vertexlist = []
edgedic = {}
needrev = []



createv()
createE()
vertexlist[1][1].counted = True
for i in bar(range(len(vertexlist)*len(vertexlist[0]))):
	lowestAll()
maze.putpixel((2,2),(255,0,0))
maze.putpixel((dimx-3,dimy-3),(255,0,0))

maze.save("mazene.png","PNG")