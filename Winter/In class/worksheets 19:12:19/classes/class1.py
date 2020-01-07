class Point():
	def __init__(self,x,y):
		self.x = x
		self.y = y

	def __str__(self):
		return(str(self.x) + " , " + str(self.y))

	def rotate90(self):
		xPositive = self.x > 0
		yPositive = self.y > 0
		if xPositive and yPositive or xPositive == False and yPositive == False:
			self.x *= (-1)
		else:
			self.y *= (-1)

	def rotate180(self):
		self.x *= (-1)
		self.y *= (-1)

	def rotaten90(self):
		self.rotate180()
		self.rotate90()

	def translate(self,x,y):
		self.x += x
		self.y += y

	def flip_horizontally(self):
		self.y *=(-1)

	def flip_vertically(self):
		self.x *=(-1)
