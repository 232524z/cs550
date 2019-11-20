#Ian
#OMH
#11/18/19
#This program generates a random maze using prim's algorithm. Points are created in a grid throught the image, seperated by 1 pixel between each point. The weights for the connections between points are randomized, and put into a dictionary where the key is the start and endpoints of the connector. The image is drawn in conjunction with the calculations. I considered making a 2 dimensional list for the maze, and putting it into an image form at the end, but I found it much easier to work with an image file for the entire time. In the original version, there was no boarder at the edge of the maze. When I showed my maze to some friends, They all suggested that I add a boarder around the maze so that it would look much more clean. I took the suggestion, and I am very happy with the results.
#Sources:Spencer, Max Fan, https://www.tutorialspoint.com/python3/python_dictionary.htm, https://pillow.readthedocs.io/en/3.1.x/reference/Image.html

import random
#point is a class, similar to a tuple, but it also contains infomration on wether the point has already been counted, and if the point is part of the gutter
from pointne import point
from PIL import Image, ImageDraw



#creates a list of points in a grid pattern given a width and height
def createv(width,height):
	vertexlist = []
	#creates vertices for every point on the grid, including gutters
	vertexlist=[[point(x,y) for y in range(height+2)] for x in range(width+2)]

	#makes the gutters be counted so they don't interfere later, and tells all of the gutter points that they are part of the gutter.
	for i in range(width):
		vertexlist[0][i].counted = True
		vertexlist[height-1][i].counted = True
		vertexlist[0][i].gutter = True
		vertexlist[height-1][i].gutter = True
	for i in range(height):
		vertexlist[i][0].counted = True
		vertexlist[i][width-1].counted = True
		vertexlist[i][0].gutter = True
		vertexlist[i][width-1].gutter = True
	#Returns the list created
	return vertexlist



#creates a list of edges between points on a grid given a width and height
def createE(width,height):
	edgedic = {}
	for i in range(width):
		for j in range(height):
			#for every edge, generates a random weight and adds it to a dictionary. The coordinates of the start point followed by the endpoint is the key.
			edgedic[((i,j),(i+1,j))]=random.random()
			edgedic[((i,j),(i,j+1))]=random.random()
	return edgedic



#Finds the edge with the lowest weight around a single point
def lowest1(x,y,vlist,edic):
	#list for the potential edges to reveal
	potentialEdges = []

	#if the points above, below, to the left, and right are not yet counted, adds the connecting edges to the list
	if vlist[x+1][y].counted == False:
		potentialEdges.append(((x,y),(x+1,y)))
	if vlist[x-1][y].counted == False:
		potentialEdges.append(((x,y),(x-1,y)))
	if vlist[x][y+1].counted == False:
		potentialEdges.append(((x,y),(x,y+1)))
	if vlist[x][y-1].counted == False:
		potentialEdges.append(((x,y),(x,y-1)))

	#smallest is the best contendor for the lowest value. The first number is the index in the list potentialedges, the second number is the weight of the edge.
	smallest = [0,1000]
	for i in range(len(potentialEdges)):
		weight = 0
		try:
			weight = edic[potentialEdges[i]]
		except:
			pass
		if weight< smallest[1]:
			smallest = [i,weight]
	#if there is a lowest value, returns the edge, and its weight
	if smallest != [0,1000]:
		return potentialEdges[smallest[0]],smallest[1]
	return None



#finds the edge with the lowest weight
def lowestAll(vlist,elist):
	#the list of all points that have been counted
	counted = []
	#adds every point that has been counted to the list
	for i in range(len(vlist)):
		for j in range(len(vlist[i])):
			if vlist[i][j].counted and vlist[i][j].gutter == False:
				counted.append(vlist[i][j])
	#smallest is the best contendor for the least weight, selected from the best contendors from each point
	smallest = [0,1000]
	for i in range(len(counted)):
		#if the new value is smaller, sets smallest to the new value
		try:
			new = lowest1(counted[i].x,counted[i].y,vlist,elist)
			if new[1]< smallest[1]:
				smallest = new
		except:
			pass

	#this should never be false, but in case there was a mistake and the lowestAll function is called to many times, this chould prevent the program from crashing
	if smallest != [0,1000]:
		#sets a and b to the x and y coordinates of the endpoint of the edge
		a,b = smallest[0][1][0],smallest[0][1][1]
		#sets x and y to the x and y coordinates of the starting point of the edge
		x,y = smallest[0][0][0],smallest[0][0][1]
		return x,y,a,b
	return None
		


#draws the connecting line. 
def drawEdges(x,y,a,b,vlist, draw):
	#The *2 is because the grid of points is half the height and width of the picture, so the coordinates need to be doubled
	draw.line(((x*2,y*2),(a*2,b*2)),(255,255,255))
	#countes the endpont of the edge
	vlist[a][b].counted = True



#draws a maze with given arguments.
def drawMaze(griddim,sizedim,name):
	"""
	the maze is always created square. griddim is the side length of the square, so it must be an intiger.
	sizedim dictates the size of the image. the image is always square, so sizedim is the side length of the sqare.
	name must be a string

	"""
	#grid is used for the grid of points, dim is used for the picture
	gridx,gridy = griddim,griddim
	dimx,dimy=gridx*2-1,gridy*2-1
	maze = Image.new("RGB",(dimx,dimy))
	#draw allows for the use of the built in line function
	draw = ImageDraw.Draw(maze)

	#creates the list of vertices
	vertexlist = createv(gridx,gridy)
	#creates the dictionary for the edges
	edgedic = createE(gridx,gridy)

	#counts the top left corner of the maze. This will allow the revealing process to start, beginning at the top left corner
	vertexlist[1][1].counted = True
	#Every point must be counted, so this reveals edges and counts points the same number of times as the total number of points. Since vertexlist is a two dimensional list, the total number of points is the width * height
	for i in range(len(vertexlist)*len(vertexlist[0])):
		lowest = lowestAll(vertexlist,edgedic)
		if lowest != None:
			#draws the edge that is returned by the lowestAll function
			drawEdges(lowest[0],lowest[1],lowest[2],lowest[3],vertexlist, draw)

	#sets the start and enpoint to red
	maze.putpixel((2,2),(255,0,0))
	maze.putpixel((dimx-3,dimy-3),(255,0,0))

	#resizes the image to 1000 by 1000 so that it doesn't appear super small, then saves the image
	maze = maze.resize((sizedim,sizedim))
	maze.save(name+".png","PNG")


#a maze can be draw with any size of the maze and image, and any name
drawMaze(20,1000,"maze")