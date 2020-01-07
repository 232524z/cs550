#Ian
#OMH
#1/7/20
#This program runs a simulation of the monty hall problem. The exact workings of the game have been simplified, but the probability is still exactly the same. I expect that the choosing to not switch doors will result in winning 33.3% of the time, since the player has a 1/3 chance of choosing the correct door. I expect that switching doors once one has been revealed will result in winning 66.7% of the time because the only way to lose is if the door originally picked contains the car. 
#Sources: None

from random import randint

#Runs a simulation for the monty hall problem where the player does not switch doors 
def stay():
	cardoor = randint(0,2)
	choice = randint(0,2)
	#the with a car behind it and the door that the player chooses are randomized
	if cardoor == choice:
		return True
	return False

#Runs a simulation for the monty hall problem where the player does switch doors 
def switch():
	cardoor = randint(0,2)
	choice = randint(0,2)
	#the with a car behind it and the door that the player chooses are randomized
	if cardoor != choice:
		return True
	return False

stayp = 0
switchp = 0
trials = 1000
for i in range(trials):
	if stay():
		stayp+=1
	if switch():
		switchp+=1

print(f'Stay: {stayp*100/trials}%')
print(f'Switch: {switchp*100/trials}%')

#The results of this program agree with what I originally thought. switching wins about 66.7% of the time, and staying wins about 33.3% of the time. When the player sticks with their original door, they lose if either of the other two doors contains the car, so their chance of losing is 2/3. since they do not do anything once of of the doors has been revealed, their chance does not change, so they lose 2/3 of the time, and win only 1/3 of the time. If the players switches, they will only lose if the car was behind the first door they guessed, so the chance of losing is 1/3, and the chance of winning is 2/3.