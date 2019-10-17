#Ian
#OMH
#10/13/19
reset()
#This program is a text based minesweeper game. This program uses recursion rather than a list to calculate the zeros. I chose to do this so that the code would be much simpler and easy to understand. At first, I started out making the board without gutters, but I quickly realized that I would drown in if statements if I continued on that path, so a switched to a with gutters board. I added a lot of error checking because I enjoyed playing the game, but while I was testing I would often forget a space, accedently type a letter, or do something else that would crash the program, and end the game preamtivly. While it is still possible to crash the program, most common errors have been fixed. One other issue I ran into while programming this was how to accept the coordinates. Years of math have taught me (x,y), but yet matrixes are defined row by column, or (y,x). I found that the most natural thing for me was (x,y), which made some things more confusing, but I thing in the end the program is more intuitive.
#Sources: Spencer

import random
import sys
from os import system, name

#resets all variables so that the game can start
def reset():
	global gameover
	global nonminespaces
	global solboard
	global showboard
	global firstmove
	gameover = False
	#number of spaces without mines, used to detect a win
	nonminespaces = ((width-2)*(height-2)-mines)
	#board with the solution
	solboard = [[0 for y in range(width)] for x in range(height)]
	#board shown to the user
	showboard = [["▣" for y in range(width)] for x in range(height)]
	#prints board and instructions
	printboard(showboard)
	print("To reveal a location, type the x coordinate followed by the y coordinate. Ex. 3 4 would reveal 3 accross and 4 down. To flag a location, type the x coordinate, the y coordinate, and the letter f. Ex. 3 4 f would place a flag at 3 across and 4 down")
	#gets the first move so that the board can be created
	while True:
		firstmove=input("move: ").split()
		if len(firstmove)>=2:
			for i in range(2):
				firstmove[i] = int(firstmove[i])
			if firstmove[0]<=width-2 and firstmove[1]<=height-2:
				break

def printboard_debug(board):
	for row in board:
		print(*row)

#displays a given board to the user
def printboard(board):
	#prints numbers at the top of the board
	print("   ", end=' ')
	for i in range(1,width-1):
		if i < 10:
			print(i, end='  ')
		else:
			print(i, end=' ')
			
	print()

	#prints the board
	for i in range(1, height-1):
		#prints numbers on the left of the board
		if i >= 10:
			print(i, end='  ')
		else:
			print(i, end='   ')
		#prints each row
		for j in range(1, width-1):
			print(board[i][j], end='  ')
		print()

#adds mines to the board, and increases numbers around the mines
def addmines():
	for i in range(mines):
		#selects a roandom location for the mine
		row = random.randint(1, height-2)
		col = random.randint(1, width-2)
		#if the location is not already a mine, and the location is not the first move of the player, puts mine there
		while(solboard[row][col] == "*" or [col, row] == firstmove):
			row = random.randint(1, height-2)
			col = random.randint(1, width-2)
		solboard[row].pop(col)
		solboard[row].insert(col, "*")
		#makes the numbers around the mine increase
		for y in range(-1, 2):
			for x in range(-1,2):
				addnumber(row+y,col+x)
	#sets the gutters to 5 so that when zeros are revealed, the gutters aren't affected
	for i in range(width):
		solboard[0][i] = 5
		solboard[height-1][i]= 5
	for i in range(height):
		solboard[i][0] = 5
		solboard[i][width-1]= 5

def addnumber(row, col):
	#if the position given is not a mine, adds one to the number
	if solboard[row][col] != "*":
		solboard[row][col] +=1

#reveals a given location on the board
def reveal(x,y):
	global nonminespaces
	global gameover
	#makes sure the location is not already revealed, and is not a gutter
	if showboard[y][x] == "▣" and y>= 1 and y<=height-2 and x>=1 and x<=width-2:
		#puts the number on the solution board into the show board
		showboard[y][x] = solboard[y][x]
		#if the number was a zero, reveals zeros around the coordinate
		if showboard[y][x] == 0:
			revealzeros(x,y)
		#if the player revealed a mine, the game ends
		if solboard[y][x] == "*":
			gameover = True
			print("\nYou lost! Game Over!")
		else:
			#if the player did not reveal a mine, decreases the non mine spaces by 1
			nonminespaces-=1
			#checks if the game has ended
			if nonminespaces == 0:
				print("\nYou won!")
				gameover = True

#goes through all surounding places and reveals the numbers
def revealzeros(x,y):
	for i in range (-1, 2):
		for z in range(-1, 2):
			reveal(x+z,y+i)

#puts a flag at a given location
def flag(x,y):
	global gameover
	#if the position is not yet revealed or flagged, places a flag
	if showboard[y][x] == "▣":
		showboard[y][x] = "⚐"
	elif showboard[y][x] == "⚐":
		#if the position is a flag, put a box there
		showboard[y][x] = "▣"

#gets the user's action and executes the appropriet function
def action():
	#takes the input and checks for errors
	while True:
		action=input("move (x,y,(f)): ").split()
		if len(action)>=2:
			for i in range(2):
				action[i] = int(action[i])
			if action[0]<=width-2 and action[1]<=height-2:
				break

	#if there are just coordinates (no flag)
	if len(action) == 2:
		reveal(action[0],action[1])
	#if there is also a flag
	elif len(action) == 3:
		flag(action[0],action[1])

#when the game ends, prints the solution, resets, and offers to play again
def gameOver():
	printboard(solboard)
	playagain = input("Play again?\n").strip().lower()
	if playagain[0] == "y":
		reset()
		gameplay()
	else:
		quit()
#clears the terminal. The clear command differs based on operation system, hence the if statemence
def clear():
	if name == "nt":
		_ = system("cls")
	else:
		_ = system("clear")

def gameplay():
	global showboard
	global solboard
	global gameover
	addmines()
	#reveals the first move
	reveal(firstmove[0],firstmove[1])
	#checks if the game has ended
	if gameover == True:
		gameOver()
		print("\n\n")
	print()
	while True:
		#clears the window so that only 1 board is visable
		clear()
		#shows the board
		printboard(showboard)
		#gets an action
		action()
		#checks if the game is over
		if gameover == True:
			gameOver()
			break

#sets the recursion limit to 20,000 so that the code can be much more concise by using recursion
sys.setrecursionlimit(20000)

#height of board and gutters
height = int(sys.argv[1])+2

#width of boeard and gutters
width = int(sys.argv[2])+2

#number of mines
mines = int(sys.argv[3])

#numbering the board does not work if the width or height of the shown board is greater than 99, and the game could crash if the board is too large, so it is limited to a 99x99 board
#makes sure the width is between 1 and 99
if width > 101 or width<1:
	while(True):
		print("Please enter a width between 1 and 99!")
		try:
			width = int(input("width: "))+2
			if width<100 and width > 0:
				break
		except ValueError:
			pass
if height > 101 or height<1:
	while(True):
		print("Please enter a height between 1 and 99!")
		try:
			height = int(input("height: "))+2
			if height<100 and height > 0:
				break
		except ValueError:
			pass

#makes sure there is at least 1 bomb, and no more than width*height bombs (maximum possible)
if mines > (width-2)*(height-2) or mines<1:
	while(True):
		print("Please enter mines between 1 and",((width-2)*(height-2)),"!")
		try:
			mines = int(input("mines: "))
			if mines<((width-2)*(height-2)) and mines > 0:
				break
		except ValueError:
			pass

reset()
gameplay()
