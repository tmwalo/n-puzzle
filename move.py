import heapq
from state import State
from copy import deepcopy

def possible_moves(parent, openset, closed, goal, hc):
	
	board = move_up(parent.board)
	if board:
		add_to_openset(openset, closed, parent, board, goal, hc)
	board = move_down(parent.board)
	if board:
		add_to_openset(openset, closed, parent, board, goal, hc)
	board = move_left(parent.board)
	if board:
		add_to_openset(openset, closed, parent, board, goal, hc)
	board = move_right(parent.board)
	if board:
		add_to_openset(openset, closed, parent, board, goal, hc)
	
def add_to_openset(openset, closed, parent, board, goal, hc):

	if in_openset(openset, board) or in_closedset(closed, board):
		return
	state = State(board, goal, parent, hc)
	print state.board
	print 'Created from: {}'.format(parent.board)
	#print 'with g = '.format(parent.g)
	heapq.heappush(openset, (state.f, state))

def in_openset(openset, board):
	if openset:
		length = len(openset)
		for i in range(length):		
			item = openset[i]
			if board == item[1].board:
				return True
	return False

def in_closedset(closed, board):
	if closed:
		length = len(closed)
		for i in range(length):
			if board == closed[i]:
				return True
	return False

def move_up(state):
	board = deepcopy(state)
	empty_tile = find_empty_tile(board)
	row = empty_tile[0]
	col = empty_tile[1]	
	if row > 0:
		tmp = board[row-1][col]
		board[row-1][col] = 0
		board[row][col] = tmp
		return board
	else:
		return None

def move_down(state):
	board = deepcopy(state)
	empty_tile = find_empty_tile(board)
	row = empty_tile[0]
	col = empty_tile[1]	
	size = len(board)
	if row < size - 1:
		tmp = board[row+1][col]
		board[row+1][col] = 0
		board[row][col] = tmp
		return board
	else:
		return None

def move_left(state):
	board = deepcopy(state)
	empty_tile = find_empty_tile(board)
	row = empty_tile[0]
	col = empty_tile[1]	
	if col > 0:
		tmp = board[row][col-1]
		board[row][col-1] = 0
		board[row][col] = tmp
		return board
	else:
		return None

def move_right(state):
	board = deepcopy(state)
	empty_tile = find_empty_tile(board)
	row = empty_tile[0]
	col = empty_tile[1]	
	size = len(state)
	if col < size - 1:
		tmp = board[row][col+1]
		board[row][col+1] = 0
		board[row][col] = tmp
		return board
	else:
		return None

def find_empty_tile(state):
	size = len(state)
	for i in range(size):
		for j in range(size):
			if state[i][j] == 0:
				tile_position = [i,j]
				return tile_position
				break
