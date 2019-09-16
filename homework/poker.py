'''
sources:https://www.programiz.com/python-programming/methods/string/strip
https://www.w3schools.com/python/python_lists.asp
https://pynative.com/python-random-shuffle/
https://snakify.org/en/lessons/two_dimensional_lists_arrays/

'''
import random
deck = []
#creates arrays of deck = []
playerHand = []
aiHand = []
publicCards = []
#creates deck
suits = [' of hearts',' of spades',' of diamonds',' of clubs']
for s in suits:
	for i in range(2, 15):
		deck.append(str(i)+s)
#gets number of opponents
opponentsNumber = int(input('how many opponents?\n'))



def shuffle():
	random.shuffle(deck)

def collectCards():
	for i in range(0,5):
		deck.append(publicCards[i])
	publicCards.clear()
	#adds players deck to the back of the deck
	deck.append(playerHand[0])
	deck.append(playerHand[1])
	#removes all cards from player's hand
	playerHand.clear()
	for i in range(0, opponentsNumber):
		#adds the cards from the ai's hand to the end of the deck
		deck.append(aiHand[i][0])
		deck.append(aiHand[i][1])
	aiHand.clear()

def dealHand():
	#deals cards to the player and ai
	playerHand.append(deck[0])
	deck.pop(0)
	playerHand.append(deck[0])
	deck.pop(0)
	for i in range(0, opponentsNumber):
		aiHand.append([deck[0],deck[1]])
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
	print("\nYour Hand\n",playerHand)
	print("\n\nTable\n",publicCards)


shuffle()
dealHand()
deal3()
deal1()
deal1()
displayCards()




