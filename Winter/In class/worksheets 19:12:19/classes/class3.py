class Student():
	def __init__(self):
		self.energy = 80
		self.hunger = 60
		self.stress = 20
		self.hours = 24

	def __str__(self):
		r = ""
		r+="\n Energy: "+ str(self.energy)
		r+="\n Hunger: "+str(self.hunger)
		r+="\n Stress: "+str(self.stress)
		r+="\n Hours: "+str(self.hours)
		return r

	def study(self,t):
		if self.hours >= t:
			self.hours -= t
			self.hunger += t*10
			self.energy -= t*20

	def sports(self,t):
		if self.hours >= t:
			self.hours -= t
			self.hunger += t*20
			self.energy -= t*15

	def Class(self,t):
		if self.hours >= t:
			self.hours -= t
			self.hunger += t*10
			self.energy -= t*20
			self.stress += t*10

	def take_test(self,t):
		if self.hours >= t:
			self.hours -= t
			self.stress += t*30

	def submit_paper(self):
		self.stress -= 20

	def eat_meal(self,t):
		if self.hours >= t:
			self.hours -= t
			self.stress -= 10*t
			self.hunger -= 10*t
			self.energy += 20*t

	def sleep(self,t):
		if self.hours >= t:
			self.hours -= t
			self.energy += 30*t
			self.hunger += 8*t

	def new_day():
		self.hours = 24