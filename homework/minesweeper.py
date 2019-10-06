import random
import sys
height = int(sys.argv[1])+2
width = int(sys.argv[2])+2
mines = int(sys.argv[3])
gameover = False
minesfound = 0
solboard = [[0 for y in range(width)] for x in range(height)]
showboard = [["▣" for y in range(width)] for x in range(height)]
firstmove=input("move: ").split()
for i in range(2):
	firstmove[i] = int(firstmove[i])

def printboard_debug(board):
	for row in board:
		print(*row)

def printboard(board):
	for row in board[1:-1]:
		print(*row[1:-1])

def addmines():
	for i in range(mines):
		row = random.randint(1, height-2)
		col = random.randint(1, width-2)
		while(solboard[row][col] == "*" or [col, row] == firstmove):
			row = random.randint(1, height-2)
			col = random.randint(1, width-2)
		solboard[row].pop(col)
		solboard[row].insert(col, "*")
		for y in range(-1, 2):
			for x in range(-1,2):
				addnumber(row+y,col+x)

def addnumber(row, col):
	if solboard[row][col] != "*":
		solboard[row][col] +=1

def reveal(x,y):
	global gameover
	showboard[y][x] = solboard[y][x]
	if showboard[y][x] == "*":
		gameover = True
		print("\nYou lost! Game Over!")

def flag(x,y):
	global minesfound
	global gameover
	if showboard[y][x] != "⚐":
		showboard[y][x] = "⚐"
		if solboard[y][x] == "*":
			minesfound += 1
	else:
		showboard[y][x] = "▣"
		if solboard[y][x] == "*":
			minesfound -= 1
	if minesfound == mines:
		print("\nYou won!")
		gameover = True



def action():
	action=input("move: ").split()
	for i in range(2):
		action[i] = int(action[i])
	if len(action) == 2:
		reveal(action[0],action[1])
	elif len(action) == 3:
		flag(action[0],action[1])



addmines()
showboard[firstmove[0]][firstmove[1]] = solboard[firstmove[0]][firstmove[1]]
while True:
	printboard(showboard)
	action()
	if gameover == True:
		printboard(showboard)
		break
	print("\n\n")

