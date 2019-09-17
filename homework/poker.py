'''
sources:https://www.programiz.com/python-programming/methods/string/strip
https://www.w3schools.com/python/python_lists.asp
https://pynative.com/python-random-shuffle/
https://snakify.org/en/lessons/two_dimensional_lists_arrays/

'''
import random
money = []
deck = []
#creates arrays of deck = []
hands = []
publicCards = []
#creates deck
suits = [' of hearts',' of spades',' of diamonds',' of clubs']
for s in suits:
	for i in range(2, 15):
		deck.append(str(i)+s)
#gets number of opponents
playerNumber = 1+int(input('how many opponents?\n'))
for i in range(0,playerNumber):
	money.append(1500)


def shuffle():
	random.shuffle(deck)

def collectCards():
	#adds public cards to the end of the deck
	for i in range(0,5):
		deck.append(publicCards[i])
	publicCards.clear()

	for i in range(0, playerNumber):
		#adds the cards from the hands to the end of the deck
		deck.append(hands[i][0])
		deck.append(hands[i][1])
	#Clears hands
	hands.clear()

def dealHand():
	#deals cards to the player and ai
	for i in range(0, playerNumber):
		hands.append([deck[0],deck[1]])
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
	print("\nYour Hand\n",hands[0])
	print("\n\nTable\n",publicCards)


def ShowOptions:
	choice = input("Fold	","Check	","Call",amountRaised,"		Raise")
	if "r" in choice:
		amountRaised = int(input("How much do you want to raise?\n")



