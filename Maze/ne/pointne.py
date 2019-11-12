class point:
	def __init__(self,x,y,w=0):
		self.x = x
		self.y = y
		self.weight = w

	def tuple(self):
		return (self.x,self.y)
		
	def __str__(self):
		return str((self.x,self.y))

	def distance(self, other):
		distance = (((self.x-other.x)**2)+((self.y-other.y)**2))
		return distance
