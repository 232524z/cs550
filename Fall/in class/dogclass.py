class Dog:
	#constructor/init
	#creates and initializes class variables/properties
	def __init__(self,age,name,energy,hunger,intelligence,speed,biteStrength):
		self.age = age
		self.name = name
		self.energy = energy
		self.hunger = hunger
		self.intelligence = intelligence
		self.speed = speed
		self.biteStrength = biteStrength
	def sleep(self):
		if self.energy > 19:
			return self.name+" rufuese to sleep any longer"
		self.energy +=1
		self.age += 1/365
		return self.name +" is sleeping"

	def stats(self):
		result = '\nName :'+self.name
		result += '\nAge: '+str(self.age)
		result += '\nEnergy: '+str(self.energy)
		result += '\nHunger: '+str(self.hunger)
		result += '\nIntelligence: '+str(self.intelligence)
		result += '\nSpeed: '+str(self.speed)
		result += '\nBite Strength: '+str(self.biteStrength)
		result += '\n'
		result += '-'*20
		return result

	def run(self):
		if self.energy < 2:
			return self.name +' refuses to run'
		self.energy -= 1
		self.hunger -= 1
		self.speed += 2
		return self.name +' is running'

	def play(self):
		if self.energy < 2:
			return self.name +'refuses to play'
		self.energy -= 1
		self.hunger -= 1
		self.speed +=1
		self.biteStrength += 1

d1 = Dog(2,"Fido",10,8,9,4,13)
d2 = Dog(5,"Abigail",8,9,10,8,11)
print(d1.play())
print(d1.run())
print(d1.play())
print(d2.sleep())
print(d1.stats())
print(d2.stats())
