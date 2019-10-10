import random
import sys
#height of board and gutters
height = int(sys.argv[1])+2
#width of boeard and gutters
width = int(sys.argv[2])+2
#numbering the board does not work if the width of the shown board is greater than 10, so the width of the board with gutters must be less than 12
if width > 12:
	while(True):
		print("Please enter a width between 1 and 10!")
		try:
			width = int(input("width: "))+2
			break
		except ValueError:
			pass
#number of mines
mines = int(sys.argv[3])

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
	#gets the first move so that the board can be created accordingly

	while True:
		firstmove=input("move (enter the x coordinate and the y coordinate of the point: ").split()
		if len(firstmove)>=2:
			for i in range(2):
				firstmove[i] = int(firstmove[i])
			if firstmove[0]<=width-2 and firstmove[1]<=height-2:
				break

reset()

def printboard_debug(board):
	for row in board:
		print(*row)

def printboard(board):
	#prints numbers at the top of the board
	print("   ", end=' ')
	for i in range(1,width-1):
		print(i, end=' ')
	print()
	print()

	for i in range(1, height-1):
		#prints numbers on the left of the board
		if i >= 10:
			print(i, end='  ')
		else:
			print(i, end='   ')
		#prints each row
		print(*board[i][1:-1])

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

def reveal(x,y):
	global nonminespaces
	global gameover
	#sets the position on the board the players sees to the number or bomb on the solution board
	if showboard[y][x] == "▣" and y>= 1 and y<=height-2 and x>=1 and x<=width-2:
		showboard[y][x] = solboard[y][x]
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

def revealzeros(x,y):
	for i in range (-1, 2):
		for z in range(-1, 2):
			reveal(x+z,y+i)


def flag(x,y):
	global gameover
	#if the position is not a flag, puts a flag there
	if showboard[y][x] != "⚐":
		showboard[y][x] = "⚐"
	else:
		#if the position is a flag, put a box there
		showboard[y][x] = "▣"

def action():
	while True:
		action=input("move (x,y,(f)): ").split()
		if len(action)>=2:
			for i in range(2):
				action[i] = int(action[i])
			if action[0]<=width-2 and action[1]<=height-2:
				break


	#if there are just coordinates
	if len(action) == 2:
		reveal(action[0],action[1])
	#if there is also a flag
	elif len(action) == 3:
		flag(action[0],action[1])

def gameOver():
	printboard(solboard)
	playagain = input("Play again?\n").strip().lower()
	if playagain[0] == "y":
		reset()
		gameplay()

def gameplay():
	global showboard
	global solboard
	global gameover
	addmines()
	#reveals the first move
	reveal(firstmove[0],firstmove[1])
	print("To reveal a location, type the x coordinate followed by the y coordinate. Ex. 3 4 would reveal 3 accross and 4 down. To flag a location, type the x coordinate, the y coordinate, and the letter f. Ex. 3 4 f would place a flag at 3 across and 4 down")
	if gameover == True:
		gameOver()
		print("\n\n")
	while True:
		printboard(showboard)
		action()
		if gameover == True:
			gameOver()
			break
		print("\n\n")
gameplay()
