#1296, 0.077
from random import randint

def trial(dice):
	l = []
	for i in range(dice):
		l.append(randint(1,6))
	return l

def score(l):
	n = l[0]
	for i in range(1,dice):
		if n != l[i]:
			return False
	return True

trials = 10000
dice = 5
for j in range(10):
	yahtzees = 0
	for i in range(trials):
		if score(trial(dice)):
			yahtzees +=1
	print(str(100*yahtzees/trials)+"%")