import random
import sys
height = int(sys.argv[1])
width = int(sys.argv[2])
mines = int(sys.argv[3])
board = [[0 for y in range(width)] for x in range(height)]
def printboard():
	for row in board:
		print(*row)

def addmines():
	for i in range(mines+1):
		row = random.randint(0, height-1)
		col = random.randint(0, width-1)
		if board[row][col] == 0:
			board[row].pop(col)
			board[row].insert(col, "*")
		else: i -= 1

def makeNumbers():
	top = False
	bottom = False
	left = False
	right = False

	for row in range(height):
		#on the top/bottom?

		if row == 0:
			top = True
		elif row == height-1:
			bottom = True


		for col in range(width):


			#on the side?
			if col == 0:
				left = True
			elif col == width-1:
				right = True


			if board[row][col] == "*":
				#top
				if top == False:
					addnumber(row-1,col)
					if left == False:
						addnumber(row-1,col-1)
					if right == False:
						addnumber(row-1,col+1)
				#left/right
				if left == False:
						addnumber(row,col-1)
				if right == False:
					addnumber(row,col+1)
				#bottom
				if bottom == False:
					addnumber(row+1,col)
					if left == False:
						addnumber(row+1,col-1)
					if right == False:
						addnumber(row+1,col+1)
			#reset
			left = False
			right = False
		top = False
		bottom = False

def addnumber(row, col):
	if board[row][col] != "*":
		board[row][col] +=1



addmines()
makeNumbers()
printboard()
