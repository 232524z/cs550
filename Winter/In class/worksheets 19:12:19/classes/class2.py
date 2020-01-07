class Bicycle():
	def __init__(self, cadence, gear, speed):
		self.cadence = cadence
		self.gear = gear
		self.speed = speed

	def __str__(self):
		return str(self.cadence)+" "+str(self.gear)+" "+str(self.speed)

	def set_gear(self, g):
		self.gear = g

	def set_cadence(self, c):
		self.cadence = c

	def apply_brake(self, b):
		self.speed -= b

	def speed_up(self, s):
		self.speed += s