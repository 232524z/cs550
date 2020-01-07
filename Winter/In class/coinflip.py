from random import random
flips = 10
for j in range(100):
	heads = 0
	for i in range(flips):
		if random()>.5:
			heads+=1
	print("Percent heads: " + str(100*heads/flips) + "%")