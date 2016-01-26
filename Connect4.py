from random import randint 
import os
import time


os.system('clear')

numRows = 7
numCols = 6
trials = 0
turn = 0
numPlayers = 2
checker = ['x', 'o', '+', '*', '#']
emptyCell_symbol = "."

players=[]
for player in range(numPlayers):
	players.append(input("Player"+str(player)+", please, enter your name: "))

print()
board = []
for row in range(numRows):
	tmpList = []
	for col in range(numCols):
		tmpList.append(emptyCell_symbol)
	board.append(tmpList)

def printBoard():
	print("  ", end="|")
	for cols in range(numCols):
		print(str(cols), end="|")
	print()

	for row in range(numRows):
		print(str(row)+" ", end="|")
		for col in range(numCols):
			print(board[row][col]+"|", end="")
		print()
	
printBoard()
print()

def winCheck(board):		#Check for win
	# Check rows
	for row in range(numRows):
		for col in range(3):
			if (board[row][col] == board[row][col + 1] == board[row][col + 2] ==\
				board[row][col + 3]) and (board[row][col] != emptyCell_symbol):
				return True

	# Check columns
	for col in range(numCols):
		for row in range(4):
			if (board[row][col] == board[row + 1][col] == board[row + 2][col] ==\
				board[row + 3][col]) and (board[row][col] != emptyCell_symbol):
				return True

	# Check diagonal (top-left to bottom-right)
	for row in range(3): 
		for col in range(3):
			if (board[row][col] == board[row + 1][col + 1] == board[row + 2][col + 2] ==\
				board[row + 3][col + 3]) and (board[row][col] != emptyCell_symbol):
				return True

	# Check diagonal (top-right to bottom-left)
	for row in range(3): 
		for col in range(5,-1,-1):
			if (board[row][col] == board[row + 1][col - 1] == board[row + 2][col - 2] ==\
				board[row + 3][col - 3]) and (board[row][col] != emptyCell_symbol):
				return True		

	# Check diagonal (bottom-left to top-right)
	for row in range(6, -1, -1):
		for col in range(3):
			if (board[row][col] == board[row - 1][col + 1] == board[row - 2][col + 2] ==\
				board[row - 3][col + 3]) and (board[row][col] != emptyCell_symbol):
				return True

	# Check diagonal (bottom-right to top-left)
	for row in range(6, -1, -1):
		for col in range(5,-1,-1):
			if (board[row][col] == board[row - 1][col - 1] == board[row - 2][col - 2] ==\
				board[row - 3][col - 3]) and (board[row][col] != emptyCell_symbol):
				return True

	# No winner: return the empty string
	return False

#GAME PLAY
turn = randint(0,numPlayers-1)
victory = False
while not victory and trials < (numCols*numRows)**2:
	print(players[turn]+", it is your turn.")

	p1guess = input("Choose your column, "+ checker[turn]+' : ')
	while not p1guess.isdigit() or not int(p1guess) in range(numCols): 
		print('User Error')
		p1guess = input("Choose your column again, "+ checker[turn]+' : ')
	p1guess = int(p1guess)

	for rows in range(numRows,0,-1):

		if board[rows-1][p1guess]==emptyCell_symbol:			#bottom
			board[rows-1][p1guess] = checker[turn]
			if winCheck(board):
				trials+=1
				print()
				printBoard()
				print()
				print(players[turn]+" Wins!")
				print(str(trials)+" turns")
				time.sleep(5)
				victory = True
				break
			trials+=1
			turn = (turn+1)%numPlayers
			break

		elif board[rows-1][p1guess]!= emptyCell_symbol and board[rows-2][p1guess]== emptyCell_symbol:		#2nd from bottom
			board[rows-2][p1guess] = checker[turn]
			if winCheck(board):
				trials+=1
				print()
				printBoard()
				print()
				print(players[turn]+" Wins!")
				print(str(trials)+" turns")
				time.sleep(5)
				victory = True
				break
			trials+=1
			turn = (turn+1)%numPlayers
			break

	print()
	os.system("clear")
	printBoard()
	print()


