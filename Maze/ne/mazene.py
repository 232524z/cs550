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
	vertexlist=[[point(x,y) for x in range(dimx+2)] for y in range(dimy+2)]

	#makes the gutters be counted so they don't interfere later
	for i in range(dimx):
		vertexlist[0][i].counted = True
		vertexlist[dimy-1][i].counted = True
		vertexlist[0][i].gutter = True
		vertexlist[dimy-1][i].gutter = True
	for i in range(dimy):
		vertexlist[i][0].counted = True
		vertexlist[i][dimx-1].counted = True
		vertexlist[i][0].gutter = True
		vertexlist[i][dimx-1].gutter = True



def createE():
	global edgedic
	for i in range(dimx):
		for j in range(dimy):
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
	counted = []
	for i in range(len(vertexlist)):
		for j in range(len(vertexlist[i])):
			if vertexlist[i][j].counted and vertexlist[i][j].gutter == False:
				counted.append(vertexlist[i][j])

	s = [0,1000]
	for i in range(len(counted)):
		w = lowest1(counted[i].x,counted[i].y)
		if w[1]< s[1]:
			s = w
	print(s)
	if s != [0,1000]:
		a,b = s[0][1][0],s[0][1][1]
		x,y = s[0][0][0],s[0][0][1]
		draw.line(((x*2,y*2),(a*2,b*2)),(255,0,0))
		vertexlist[x][y].counted = True







# def reveal(x,y):
# 	global vertexlist
# 	vertexlist[x][y].counted = True
# 	l = []

# 	if vertexlist[x+1][y].counted == False:
# 		l.append((x,y),(x+1,y))
# 	if vertexlist[x-1][y].counted == False:
# 		l.append((x,y),(x-1,y))
# 	if vertexlist[x][y+1].counted == False:
# 		l.append((x,y),(x,y+1))
# 	if vertexlist[x][y-1].counted == False:
# 		l.append((x,y),(x,y-1))

# 	s = [0,1000]
# 	for i in range(len(l)):
# 		w = edgedic[l[i]]
# 		if w< s[1]:
# 			s = [i,w]
# 	if s != [0,1000]:
# 		a,b=l[s[0]][0][0],l[s[0]][0][1]
# 		draw.line(((x*2,y*2),(a*2,b*2)),(255,0,0))
# 		reveal(l[s[0]][0],l[s[0]][1])







dimx,dimy=10,10
maze = Image.new("RGB",(dimx*2,dimy*2))
draw = ImageDraw.Draw(maze)
vertexlist = []
edgedic = {}
needrev = []



createv()
createE()
vertexlist[1][1].counted = True
for i in range(len(vertexlist)):
	lowestAll()





maze.save("mazene.png","PNG")