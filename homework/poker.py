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
	def __init__(self, pos):
		self.hand = []
		self.handNumbers =[]
		self.money = 1500
		self.handQuality = 0
		self.willBet = 0
		self.inRound = True
		self.pos = pos
#determines how much to bet
	def betCalc(self):
		global tableMoney
		global amountRaised
		if len(publicCards) == 0:
			self.willBet = 5*(random.randint(0,10))+self.handQuality
		elif len(publicCards) == 3:
			self.willBet = 15*(random.randint(0,10))+5*self.handQuality
		elif len(publicCards) >=4:
			self.willBet =15*(random.randint(0,10))+10*self.handQuality
		while(self.willBet>self.money):
			self.willBet*(3/4)

	def bet(self, name):
		global playersFolded
		global amountRaised
		global playersChecked
		global userRaised
		if self.inRound == True:
			if amountRaised==0:
				self.lose((3/4)*self.willBet)
				amountRaised = round((3/4)*self.willBet)
				print("Player",name+1,"raised",amountRaised)
				playersChecked = 0
				playerRaised = self.pos
				userRaised = False
			elif amountRaised < self.willBet:
				if self.willBet/1.3 > amountRaised:
					self.lose((3/4)*self.willBet)
					amountRaised += (round((3/4)*self.willBet)-amountRaised)
					print("Player",name+1,"raised",amountRaised)
					playersChecked = 0
					playerRaised = self.pos
					userRaised = False
				else:
					self.lose(amountRaised)
					print("Player",name+1,"called")
					playersChecked+=1
			elif self.inRound == True:
				self.inRound = False
				print("Player",name+1,"folded")
				playersFolded += 1
		if self.handQuality > 2000:
			self.handQuality = 2000

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
		self.handNumbers =[]
		self.money = 1500
		self.handQuality = 0
	def give(self, card):
		self.hand.append(card)

	def calcQ(self):
		Round = 5
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
tableMoney = 0
amountRaised = 0
playerNumber = 0
playerRaised = 0
playersChecked = 0
userRaised = False
playersFolded = 0
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
			if playerNumber > 0 and playerNumber <= 22:
				break
			else: print("Please enter a number between 1 and 22!")
		except ValueError:
			print("Please enter an integer")
	for i in range(playerNumber):
	#adds opponets to the ai array
		ai.append(Opponent(i))
	print("\n\n\n\n")

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
	print("\nMoney:",player.money)
	for i in range(playerNumber):
		print("\nPlayer",(i+1),"'s money:",ai[i].money)
	print("\n")

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
	global playersChecked
	winner = highHand()
	ai[winner].give(tableMoney)
	tableMoney = 0
	print("Player",str(winner+1),"Wins!")

def call(): 
	global tableMoney
	global amountRaised
	global playersChecked
	player.money-=amountRaised
	tableMoney+=amountRaised
	playersChecked +=1

def Raise():
	global tableMoney
	global amountRaised
	global playersChecked
	response = int(input("How much do you want to raise?\n"))
	if response<amountRaised:
		print("Not enough! Automatically checking")
	else:
		amountRaised = response-amountRaised
		playersChecked = 0
		player.money -= response
		tableMoney += response
		userRaised = True
		playRound()

def playRound():
	global playerNumber
	displayCards()
	for i in range(playerNumber):
		ai[i].betCalc()
		ai[i].bet(i)
	if playersFolded != playerNumber:
		showOptions()
	if amountRaised != 0 and userRaised == False:
		for i in range(playerRaised):
			ai[i].betCalc()
			ai[i].bet(i)
	if playerRaised != 0:
		for i in range(playerRaised):
			ai[i].betCalc()
			ai[i].bet(i)
	print("*"*60)
	print("\n"*5)



def getReadyForNextRound():
	playersChecked = 0
	userRaised = False
	amountRaised = 0
	print()
def gameplay():
	global playersChecked
	global userRaised
	global amountRaised
	global tableMoney
	while(True):
		startup()
		shuffle()
		dealHand()
		playRound()
		getReadyForNextRound()
		if playersFolded == playerNumber:
			print("You won this round!")
			break
		deal3()
		playRound()
		getReadyForNextRound()
		if playersFolded == playerNumber:
			print("You won this round!")
			break
		deal1(3)
		playRound()
		getReadyForNextRound()
		if playersFolded == playerNumber:
			print("You won this round!")
			break
		deal1(4)
		playRound()
		if playersFolded != playerNumber:
			winnerlist = [0,0]
			for i in range(playerNumber):
				ai[i].calcQ(5)
			for i in range(playerNumber):
				if ai[i].handQuality> winnerlist[0]:
					winnerlist.clear()
					winnerlist.append(ai[i].handQuality)
					winnerlist.append(ai[i].pos)
			player.calcQ()
			if winnerlist[0]>player.handQuality:
				print("Player",(winnerlist[1]+1),"won!")
				ai[winnerlist[1]].money += tableMoney
				tableMoney = 0
			else:
				print("You won this round!")
				player.hand += tableMoney
				tableMoney = 0
		if playersFolded == playerNumber:
			print("You won this round!")
		break
			




gameplay()
'''
Note: The game does not work
Comments:

Spencer: Game broke when I put in 999999999999 for the amount of opponents I wanted
Please fix

Stanley: Do a restart thing where the player is given the option to restart the game. 


Kate: I was a little confused on how to play this, maybe you could add
instructions? I know it's a draft though so no worries! I like the
green text + black background, very eye-catching!

Nicole: I think you should give the option of reading the rules of how to play blackjack. Also it was a bit unclear what to type when "Fold Check Call Raise" appeared so maybe in parenthesis saying to type either of those words down would be helpful.

Ting: I agree with some people from above, make sure to include instructions. Other than that, you're really close to finishing the game.

Chandler: I don't know how to play poker so I can give absolutely no input on this game
Except maybe to add instructions. But it looks cool!










'''