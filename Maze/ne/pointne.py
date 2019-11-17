class point:
	def __init__(self,x,y):
		self.x = x
		self.y = y
		self.counted = False
		self.gutter = False

	def tuple(self):
		return (self.x,self.y)
		
	def __str__(self):
		if self.counted == False:
			return "0"
		return "1"

	def distance(self, other):
		distance = (((self.x-other.x)**2)+((self.y-other.y)**2))
		return distance
