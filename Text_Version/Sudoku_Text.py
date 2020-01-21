# Text based Sudoku solver using Backtracking Algorythm

# Hard
board = [
	[0,3,8,0,0,0,0,0,0],
    [0,0,0,4,0,0,9,0,0],
    [2,0,0,0,0,0,1,0,5],
    [7,0,5,2,0,0,0,0,0],
    [8,0,0,3,0,5,0,0,6],
    [0,0,0,0,0,1,2,0,7],
    [3,0,7,0,0,0,0,0,4],
    [0,0,9,0,0,4,0,0,0],
    [0,0,0,0,0,0,6,3,0]
]

# Easy
board = [
	[7,0,0,4,0,1,0,0,0],
    [0,2,3,5,0,0,1,0,0],
    [6,0,0,7,8,0,0,0,0],
    [4,5,0,0,1,0,0,0,6],
    [2,7,8,0,9,0,1,5,3],
    [1,0,0,0,5,0,0,8,4],
    [0,0,0,0,7,6,0,0,9],
    [0,4,0,0,0,5,8,6,0],
    [0,0,0,9,0,8,0,0,2]
]
tries = 0


def print_board(board):
	"""
	Prints the sudoku board
	:paramiter board: A 2D list of integers
	:returns: None
	"""
	for i in range(len(board)):
		if i % 3 == 0 and i != 0:
			print("-----------------------")

		for j in range(len(board[0])):
			if j % 3 == 0 and j != 0:
				print(" | ", end = "")

			if j != 8:
				print(str(board[i][j]) + " ", end = "")
			else:
				print(str(board[i][j]))


def solve(board):
	"""
	Solves the sudoku board, using backtracking and recursion
	:parameter board: A 2D list of integers
	:return: boolean (True or False)
	"""
	print("----------")
	print(board)
	times()

	find = ()
	find = find_empty_square(board)
	if not find:
		return True
	else:
		row, col = find

	for i in range(1, 10):
		if valid(board, i, (row, col)):
			board[row][col] = i

			if solve(board):
				return True
			else:
				board[row][col] = 0

	return False


def times():
	global tries
	tries += 1
	return tries



def find_empty_square(board):
	"""
	Find empty squares in the sudoku board
	:parameter board: A 2D list of integers
	:returns (i, j): a tuple containing the coardinate of the empty board
	"""
	for i in range(len(board)):
		for j in range(len(board[i])):
			if board[i][j] == 0:
				return (i, j)
				break

	return None


def valid(board, number, position):
	"""
	Check the selected number is valid at the position or not
	:parameter: 3 parameters
			board: A 2D list of integers
			number: selected integer
			position: tuple of integers returned by find_empty_square()
	:returns : boolean (True or False)
	"""

	# Checking the validation in row
	for i in range(len(board)):
		if board[position[0]][i] == number and position[1] != i:
			return False

	# Checking the validation in culumn
	for i in range(len(board)):
		if board[i][position[1]] == number and position[0] != i:
			return False

	# Check the validation in small boxes
	box_x = position[1] // 3
	box_y = position[0] // 3

	for i in range(box_y * 3, box_y * 3 + 3):
		for j in range(box_x * 3, box_x * 3 + 3):
			if board[i][j] == number and (i, j) != position:
				return False

	return True


print_board(board)
solve(board)
print("----Solved----")
print_board(board)
print("number of tries to solve: " + str(times()))