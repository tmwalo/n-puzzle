from npuzzle_mod import Board
import random

def generate_random_array(size):
	if size < 3:
		return None
	index = 0
	board_1d = []
	while index < (size**2):
		board_1d.append(index)
		index += 1
	current_index = (size**2) - 1
	while current_index > 0:
		random_index = random.randint(0, current_index)
		temp = board_1d[current_index]
		board_1d[current_index] = board_1d[random_index]
		board_1d[random_index] = temp
		current_index -= 1
	return board_1d
