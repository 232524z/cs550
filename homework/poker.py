'''
sources:https://www.programiz.com/python-programming/methods/string/strip
https://www.w3schools.com/python/python_lists.asp
https://pynative.com/python-random-shuffle/
https://snakify.org/en/lessons/two_dimensional_lists_arrays/

'''
import random
#creates arrays of cards
cards = []
playerHand = []
aiHand = []
#creates cards
suits = ['h','s','d','c']
for s in suits:
	for i in range(2, 15):
		cards.append(str(i)+s)
#gets number of opponents
opponentsNumber = int(input('how many opponents?\n'))



def shuffle():
	random.shuffle(cards)

def collectCards():
	#adds players cards to the back of the deck
	cards.append(playerHand[0])
	cards.append(playerHand[1])
	#removes all cards from player's hand
	playerHand.clear()
	for i in range(0, opponentsNumber):
		#adds the cards from the ai's hand to the end of the deck
		cards.append(aiHand[i][0])
		cards.append(aiHand[i][1])
	aiHand.clear()

def dealHand():
	#deals cards to the player and ai
	playerHand.append(cards[0])
	cards.pop(0)
	playerHand.append(cards[0])
	cards.pop(0)
	for i in range(0, opponentsNumber):
		aiHand.append([cards[0],cards[1]])
		cards.pop(0)
		cards.pop(0)



shuffle()
dealHand()
print(playerHand)
print(aiHand)
collectCards()
shuffle()
dealHand()
print(playerHand)
print(aiHand)





