import random
class edge:
	def __init__(self,p1,p2,d):
		self.p1 = p1
		self.p2 = p2
		self.w = random.random()
		self.d = d

	def __str__(self):
		return str(round(self.w))

	def draw(self):
		draw.line(((p1.x,p1.y),p2.x,p2.y),(255,0,0))