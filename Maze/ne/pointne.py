#custom class point. It holds the x and y coordinates for a point, along with wether or not the point has been counted in the maze generation algorithm, and wether it is part of the gutters
class point:
	def __init__(self,x,y):
		self.x = x
		self.y = y
		self.counted = False
		self.gutter = False

	#returns the coordinates when a string is required. Used for debugging
	def __str__(self):
		return str((self.x,self.y))