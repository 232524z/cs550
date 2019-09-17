'''
sources:https://www.programiz.com/python-programming/methods/string/strip
https://www.w3schools.com/python/python_lists.asp
https://pynative.com/python-random-shuffle/
https://snakify.org/en/lessons/two_dimensional_lists_arrays/
https://docs.python.org/3/tutorial/classes.html
'''
import random

class Opponent:
	def __init__(self):
		self.hand = []
		self.handNumbers =[]
		self.money = 1500
		self.bluff = False
		self.handQuality = 0

	def give(self, card):
		self.hand.append(card)
	def lose(self, ammount):
		self.money -= ammount
	def gain(self, ammount):
		self.money += amount
	def calcQ():
		handQuality = 0




class Player:
	money = 1500
	def __init__(self):
		self.hand = []
	def give(self, card):
		self.hand.append(card)


#creates array of AIs
ai = []
#creates player
player = Player()
#creates arrays of cards
deck = []
#creates the array for cards on the table
publicCards = []


#creates deck
suits = [' of hearts',' of spades',' of diamonds',' of clubs']
for s in suits:
	for i in range(2, 15):
		deck.append(str(i)+s)


#gets number of opponents
while True:
	try:
		playerNumber = input('how many opponents?\n')
		playerNumber = int(playerNumber)
		break
	except ValueError:
		print("Please enter an integer!")


for i in range(0,playerNumber):
	#adds opponets to the ai array
	ai.append(Opponent())
	



def shuffle():
	random.shuffle(deck)


def collectCards():
	#adds public cards to the end of the deck
	for i in range(0,5):
		deck.append(publicCards[i])
	publicCards.clear()
	
	#adds the cards from the hands to the end of the deck
	for i in range(0, playerNumber):
		deck.append(ai[i].hand[0])
		deck.append(ai[i].hand[1])
		ai[i].hand.clear()


def dealHand():
	
	#deals cards to the player
	player.give(deck[0])
	player.give(deck[1])
	deck.pop(0)
	deck.pop(0)

	#deals cards to the and ai
	for i in range(0, playerNumber):
		ai[i].give(deck[0])
		ai[i].give(deck[1])
		deck.pop(0)
		deck.pop(0)




def deal3():
	#burn 1
	deck.append(deck[0])
	deck.pop(0)
	#deal 3
	for i in range(0,3):
		publicCards.append(deck[0])
		deck.pop(0)

def deal1():
	#burn 1
	deck.append(deck[0])
	deck.pop(0)
	#deal 1
	publicCards.append(deck[0])
	deck.pop(0)

def displayCards():
	print("\nYour Hand\n",player.hand)
	print("\n\nTable\n",publicCards)


def showOptions():
	while True:
		choice = input("Fold	","Check	","Call",amountRaised,"		Raise").strip().lower()
		if choice == "fold":
			fold()
			break
		elif choice == "check":
			check()
			break
		elif choice == "call":
			call()
			break
		elif choice == "raise":
			Raise()
			break
		else: print("Please choose one of the options!")
	'''
def fold():
	#fold

def check():
	#check

def call(): 
	#call

def Raise():
	#raise
'''
def gameplay():
	shuffle()
	dealHand()
	displayCards()
	deal3()
	displayCards()
	deal1()
	displayCards()
	deal1()
	displayCards()

gameplay()


























