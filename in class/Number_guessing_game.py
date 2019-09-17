
import random
thenumber = random.randint(1,100)
print("Im thinking of a number between 1 and 100\n")
def numberGame():
	tries = 10
	while(True):
		if tries < 0:
			print("Oh no! You ran out of tries!")
			break
		userguess = input("Guess >>>")
		try:
			userguess = int(userguess)
			if userguess == thenumber:
				print("you got it! Thanks for playing.")
				break
			elif userguess > thenumber:
				print("The number is LESS than",userguess)
				tries-=1
			elif userguess < thenumber:
				print("The number is GREATER than ",userguess)
				tries-=1
		except ValueError:
			print('Please enter integer!')

numberGame()
