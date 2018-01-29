import re

def is_comment(token):
	if isinstance(token, str) and (token != ""):
		split_tokens = re.split("\s+", token)
		split_tokens = list(filter(None, split_tokens))
		if not split_tokens:
			return False
		if split_tokens[0].startswith("#"):
			return True
	return False

def npuzzle_size(token):
	if isinstance(token, str) and (token != ""):
		split_tokens = re.split("\s+", token)
		split_tokens = list(filter(None, split_tokens))
		if not split_tokens:
			return False
		index = 0
		while index in range(len(split_tokens)):
			if index == 0:
				try:
					puzzle_size = int(split_tokens[index])
					if puzzle_size < 3:
						return False
				except ValueError:
					return False
			if index == 1:
				if is_comment(split_tokens[index]):
					return True
				else:
					return False
			index += 1
		return True
	else:
		return False

def store_npuzzle_size(token):
	if npuzzle_size(token):
		split_tokens = re.split("\s+", token)
		split_tokens = list(filter(None, split_tokens))
		return int(split_tokens[0])
	else:
		return False

def validate_npuzzle_row(token, size):
	if size < 3:
		return False
	if isinstance(token, str) and (token != ""):
		split_tokens = re.split("\s+", token)
		split_tokens = list(filter(None, split_tokens))
		if not split_tokens:
			return False
		index = 0
		while index in range(len(split_tokens)):
			if index < size:
				try:
					cell_value = int(split_tokens[index])
					if cell_value < 0 or cell_value >= (size * size):
						return False
				except ValueError:
					return False
			else:
				if is_comment(split_tokens[index]):
					return True
				else:
					return False
			index += 1
		if index < size:
			return False
		else:
			return True
	else:
		return False

def store_npuzzle_row(token, size):
	if validate_npuzzle_row(token, size):
		split_tokens = re.split("\s+", token)
		split_tokens = list(filter(None, split_tokens))
		npuzzle_row = []
		index = 0
		while index < size:
			npuzzle_row.append(split_tokens[index])
			index += 1
		return npuzzle_row
	else:
		return False

def validate_sequence(board, puzzle_size):
	if len(board) != puzzle_size:
		return False
	index = 0
	sequence = []
	while index < (puzzle_size * puzzle_size):
		sequence.append(False)
		index += 1
	for cell_row in board:
		for cell in cell_row:
			if cell < (puzzle_size * puzzle_size):
				if sequence[cell] == False:
					sequence[cell] = True
				else:
					return False
	if False in sequence:
		return False
	else:
		return True
