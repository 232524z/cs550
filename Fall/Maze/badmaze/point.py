class point:
	def __init__(self,x,y):
		self.x = x
		self.y = y

	def tuple(self):
		return (self.x,self.y)
		
	def __str__(self):
		return str((self.x,self.y))

	def distance(self, other):
		dif1 = self.x-other.x
		dif2 = self.y-other.y
		distance = (dif1*dif1)+(dif2*dif2)
		return distance
