class vertex:
	def __init__(self):
		self.vertices = []

	def __str__(self):
		result = ""
		for i in range(len(self.vertices)):
			result += str(self.vertices[i])
		return result
		
	def __len__(self):
		return len(self.vertices)

	def closest(self,other):
		smallestD = 100000
		smallestI = [0,0]
		for i in range(len(self)):
			for j in range(len(other)):
				d = self.vertices[i].distance(other.vertices[j])
				if smallestD > d:
					smallestD = d
					smallestI = [i,j]
		return smallestI[1],[self.vertices[smallestI[0]],other.vertices[smallestI[1]]]

	def remove(self,I):
		self.vertices.pop(I)
	def add(self,p):
		self.vertices.append(p)