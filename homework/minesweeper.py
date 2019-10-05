import random
import sys
height = int(sys.argv[1])+2
width = int(sys.argv[2])+2
mines = int(sys.argv[3])
board = [[0 for y in range(width)] for x in range(height)]
firstmove=int(input("move: ").split())

def printboard_debug():
	for row in board:
		print(*row)

def printboard():
	for row in board[1:-1]:
		print(*row[1:-1])

def addmines():
	for i in range(mines+1):
		row = random.randint(1, height-2)
		col = random.randint(1, width-2)
		if board[row][col] != "*" and [col, row] != [firstmove]:
			print([row, col])
			print(firstmove)
			board[row].pop(col)
			board[row].insert(col, "*")
			for y in range(-1, 2):
				for x in range(-1,2):
					addnumber(row+y,col+x)
		else: i -= 1

def addnumber(row, col):
	if board[row][col] != "*":
		board[row][col] +=1



addmines()
printboard()
