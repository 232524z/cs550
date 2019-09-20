'''
sources:https://www.programiz.com/python-programming/methods/string/strip
https://www.w3schools.com/python/python_lists.asp
https://pynative.com/python-random-shuffle/
https://snakify.org/en/lessons/two_dimensional_lists_arrays/
https://docs.python.org/3/tutorial/classes.html
https://www.geeksforgeeks.org/python-randint-function/
Spencer
'''
import random

class Opponent:
	def __init__(self):
		self.hand = []
		self.handNumbers =[]
		self.money = 1500
		self.bluff = False
		self.handQuality = 0
		self.willBet = 0
		self.inRound = True
#determines how much to bet
	def betCalc(self):
		global tableMoney
		global amountRaised
		if self.bluff == True:
			self.willBet = (random.randint(0,round(self.money/5))+self.money)*(1/2)
		else:
			if len(publicCards) == 0:
				if self.handQuality < 5:
					self.willBet = 0
					self.inRound = False
				elif self.handQuality>100:
					self.willBet = (random.randint(0,round(self.money/5))+self.money)*(3/4)
				else:
					self.willBet = self.money*(self.handQuality/3000)

			if len(publicCards) == 5:
				if self.handQuality < 150:
					self.willBet = 0
					self.inRound = False
				elif self.handQuality>2000:
					self.willBet = (random.randint(0,(self.money/5))+self.money)*(3/4)
				else:
					self.willBet = self.money*(self.handQuality/3000)


	def bet(self, name):
		global amountRaised
		betThisRound = self.willBet*(random.randint(8,12))/10
		if self.inRound == True and amountRaised:
			if amountRaised==0:
				self.lose((3/4)*betThisRound)
				amountRaised = round((3/4)*betThisRound)
				print("Player",name,"raised",amountRaised)
			elif amountRaised < self.willBet:
				self.lose(amountRaised)
				print("Player",name,"called")
			elif self.inRound == True:
				self.inRound = False
				print("Player",name,"folded")

	def give(self, card):
		self.hand.append(card)

	def lose(self, amount):
		amount = round(amount)
		self.money -= amount
		global tableMoney
		tableMoney += amount

	def gain(self, amount):
		amount = round(amount)
		self.money += amount

	def calcQ(self, Round):
		if Round == 1 and random.randint(0,100)<10:
			self.bluff = True
		card1value = int(self.hand[0].split()[0])
		card1suite = self.hand[0].split(str(card1value))[1]
		card2value = int(self.hand[1].split()[0])
		card2suite = self.hand[1].split(str(card2value))[1]
		#makes a starting hand quality value based on numbers
		if card1value>card2value:
			self.handQuality = card1value
		else: self.handQuality = card2value
		#each potentially good quality increases hand quality e.g. pair, potential straight, potential flush etc.
		if abs(card1value-card2value) <=3:
			self.handQuality*=2
		if card1value == card2value:
			self.handQuality*=8
		#compaiers suits of cards
		if card1suite == card2suite:
			self.handQuality*=2
		#if there are cards on the table
		if Round >= 3:
			for i in range(0,3):
				#potential straight
				if abs(card1value-publicCardsValue[i])<3 and abs(card1value-card2value)<3:
					self.handQuality*=2
				if abs(card2value-publicCardsValue[i])<3 and abs(card2value-card2value)<3:
					self.handQuality*=2
				#potential flush
				if publicCardsSuite[i]==card1suite or publicCardsSuite[i]==card2suite:
					self.handQuality*=2
				#pair/three of a kind
				if publicCardsValue[i]==card1suite or publicCardsValue[i]==card2value:
					self.handQuality*=8
		if Round >= 4:
			#potential straight
			if abs(card1value-publicCardsValue[3])<3 and abs(card1value-card2value)<3:
					self.handQuality*=2
			if abs(card2value-publicCardsValue[3])<3 and abs(card2value-card2value)<3:
					self.handQuality*=2
			#potential flush
			if publicCardsSuite[3]==card1suite or publicCardsSuite[i]==card2suite:
					self.handQuality*=2
			#pair/three of a kind/four of a kind/full house
			if publicCardsValue[3]==card1suite or publicCardsValue[i]==card2value:
					self.handQuality*=8
		if Round == 5:
			#potential straight
			if abs(card1value-publicCardsValue[4])<3 and abs(card1value-card2value)<3:
					self.handQuality*=2
			if abs(card2value-publicCardsValue[4])<3 and abs(card2value-card2value)<3:
					self.handQuality*=2
			#potential flush
			if publicCardsSuite[4]==card1suite or publicCardsSuite[i]==card2suite:
					self.handQuality*=2
			#pair/three of a kind/four of a kind/full house
			if publicCardsValue[4]==card1suite or publicCardsValue[i]==card2value:
					self.handQuality*=8

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
publicCardsValue = []
publicCardsSuite = []
playerRaised = False
tableMoney = 0
amountRaised = 0
playerNumber = 0
#creates deck
suits = [' of hearts',' of spades',' of diamonds',' of clubs']
for s in suits:
	for i in range(2, 15):
		deck.append(str(i)+s)

#starts up the game
def startup():
	play = input("Are you ready to play? (Yes/No)\n").strip().lower()
	while True:
		if play[0] == "n":
			exit()
		if play[0] == "y":
			break
		else:
			play = input("Please enter Yes or No!\n").strip().lower()
	
	#gets number of opponents
	while True:
		global playerNumber
		try:
			playerNumber = int(input('how many opponents?\n'))
			break
		except ValueError:
			print("Please enter an integer!")
	for i in range(playerNumber):
	#adds opponets to the ai array
		ai.append(Opponent())

#shuffles deck
def shuffle():
	random.shuffle(deck)

#collects cards and puts them back in the deck
def collectCards():
	#adds public cards to the end of the deck
	for i in range(0,5):
		deck.append(publicCards[i])
	publicCards.clear()
	
	#adds the cards from the hands to the end of the deck
	for i in range(playerNumber):
		deck.append(ai[i].hand[0])
		deck.append(ai[i].hand[1])
		ai[i].hand.clear()
	#clears public card suites and values
	publicCardsSuite.clear()
	publicCardsValue.clear()

#deals everyone their cards
def dealHand():
	#deals cards to the player
	player.give(deck[0])
	player.give(deck[1])
	deck.pop(0)
	deck.pop(0)

	#deals cards to the and ai
	for i in range(playerNumber):
		ai[i].give(deck[0])
		ai[i].give(deck[1])
		deck.pop(0)
		deck.pop(0)

#deals 3 cards to the table
def deal3():
	#burn 1
	deck.append(deck[0])
	deck.pop(0)
	#deal 3
	for i in range(0,3):
		publicCards.append(deck[0])
		publicCardsValue.append(int(deck[0].split()[0]))
		publicCardsSuite.append(deck[0].split(str(publicCardsValue[i]))[1])
		deck.pop(0)

#deals one card to the table
def deal1(Round):
	#burn 1
	deck.append(deck[0])
	deck.pop(0)
	#deal 1
	publicCards.append(deck[0])
	publicCardsValue.append(int(deck[0].split()[0]))
	publicCardsSuite.append(deck[0].split(str(publicCardsValue[Round]))[1])
	deck.pop(0)

#finds which ai has the best cards
def highHand():
	Max=0
	maxai=0
	for i in range(playerNumber):
		ai[i].calcQ(len(publicCards))
		if ai[i].handQuality>Max:
			Max=ai[i].handQuality
			maxai=i
	return maxai

#show player cards
def displayCards():
	print("\nYour Hand\n",player.hand)
	print("\n\nTable\n",publicCards)

#shows player what they can do
def showOptions():
	while True:
		print("\nFold		Check		Call",amountRaised,"		Raise")
		choice = (input("\n")).lower().strip()
		if choice == "fold":
			fold()
			break
		elif choice == "check":
			if amountRaised!=0:
				print("Can't check. Automatically calling",amountRaised)
				call()
				break
		elif choice == "call":
			call()
			break
		elif choice == "raise":
			Raise()
			break
		else: print("Please choose one of the options!")

#player folds
def fold():
	global tableMoney
	winner = highHand()
	ai[winner].give(tableMoney)
	tableMoney = 0
	print("Player",str(winner+1),"Wins!")

def call(): 
	global tableMoney
	global amountRaised
	player.money-=amountRaised
	tableMoney+=amountRaised

def Raise():
	global playerRaised
	playerRaised = True

def gameplay():
	global amountRaised
	global playerRaised
	startup()
	shuffle()
	dealHand()
	if playerRaised == True:
		playerRaised = False
		for i in range(playerNumber):
			ai[i].calcQ(1)
			ai[i].betCalc()
			ai[i].bet(i+1)
		showOptions()
	if playerRaised == True:
		playerRaised = False
		for i in range(playerNumber):
			ai[i].calcQ(1)
			ai[i].betCalc()
			ai[i].bet(i+1)
		showOptions()
	exit()
gameplay()












