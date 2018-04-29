def coordinates(state, board_size, value):
	row = 0
	while row < board_size:
		column = 0
		while column < board_size:
			if state[row][column] == value:
				return {"x": column, "y": row}
			column += 1
		row += 1

def cell_manhattan_dist(state, goal, board_size, value):
	board_coord = coordinates(state, board_size, value)
	goal_coord = coordinates(goal, board_size, value)
	return abs(board_coord["x"] - goal_coord["x"]) + abs(board_coord["y"] - goal_coord["y"])

def manhattan_distance(state, goal, board_size):
	index = 1
	heuristic = 0
	while index < board_size**2:
		heuristic += cell_manhattan_dist(state, goal, board_size, index)
		index += 1
	return heuristic

def hamming_distance(state, goal, board_size):
	index = 1
	heuristic = 0
	while index < board_size**2:
		if cell_manhattan_dist(state, goal, board_size, index):
			heuristic += 1
		index += 1
	return heuristic

def cell_out_of_row_and_column(state, goal, board_size, value):
	board_coord = coordinates(state, board_size, value)
	goal_coord = coordinates(goal, board_size, value)
	out_of_row_and_column = 0
	if (board_coord["x"] - goal_coord["x"]):
		out_of_row_and_column += 1
	if (board_coord["y"] - goal_coord["y"]):
		out_of_row_and_column += 1
	return out_of_row_and_column

def out_of_row_and_column(state, goal, board_size):
	index = 1
	heuristic = 0
	while index < board_size**2:
		heuristic += cell_out_of_row_and_column(state, goal, board_size, index)
		index += 1
	return heuristic

def heuristic(state, goal, board_size, hc):
	if hc == 1:
		return manhattan_distance(state, goal, board_size)
	if hc == 2:
		return hamming_distance(state, goal, board_size)
	else:
		return out_of_row_and_column(state, goal, board_size)

def get_depth(state):
	if state:
		return (state.g + 1)
	else:
		return 0

