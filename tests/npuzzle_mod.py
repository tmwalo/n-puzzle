# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    npuzzle_mod.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: tmwalo <marvin@42.fr>                      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/01/30 15:13:29 by tmwalo            #+#    #+#              #
#    Updated: 2018/01/30 16:37:12 by tmwalo           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import re
import sys
from copy import deepcopy

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
			npuzzle_row.append(int(split_tokens[index]))
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

def build_npuzzle():
	npuzzle_file = sys.stdin.read().splitlines()
	if not npuzzle_file or "" in npuzzle_file:
		return False
	board_size = 0
	npuzzle = []
	for line in npuzzle_file:
		if not is_comment(line):
			if not board_size:
				board_size = store_npuzzle_size(line)
				if not board_size:
					return False
			else:
				npuzzle_row = store_npuzzle_row(line, board_size)
				if npuzzle_row:
					npuzzle.append(npuzzle_row)
				else:
					return False
	if validate_sequence(npuzzle, board_size):
		return npuzzle
	else:
		return False

class Board:

	def __init__(self, board):
		self.board = board
		self.size = len(board[0])
		self.goal_board = None
	
	def get_size(self):
		return self.size

	def coordinates(self, value):
		row = 0
		while row < self.get_size():
			column = 0
			while column < self.get_size():
				if (self.board)[row][column] == value:
					return {"x": column, "y": row}
				column += 1
			row += 1

	def cell_manhattan_dist(self, value):
		board_coord = self.coordinates(value)
		goal_coord = (self.goal_state()).coordinates(value)
		return abs(board_coord["x"] - goal_coord["x"]) + abs(board_coord["y"] - goal_coord["y"])

	def manhattan_distance(self):
		index = 1
		heuristic = 0
		while index < (self.get_size())**2:
			heuristic += self.cell_manhattan_dist(index)
			index += 1
		return heuristic

	def board_spiral_translate(self):
		board_list = []
		row_index = 0
		rem_rows = self.size
		column_index = 0
		rem_columns = self.size
		while row_index < rem_rows and column_index < rem_columns:
			index = column_index
			while index < rem_columns:
				if self.board[row_index][index]:
					board_list.append(self.board[row_index][index])
				index += 1
			row_index += 1
			index = row_index
			while index < rem_rows:
				if self.board[index][rem_columns - 1]:
					board_list.append(self.board[index][rem_columns - 1])
				index += 1
			rem_columns -= 1
			if row_index < rem_rows:
				index = rem_columns - 1
				while index >= column_index:
					if self.board[rem_rows - 1][index]:
						board_list.append(self.board[rem_rows - 1][index])
					index -= 1
				rem_rows -= 1
			if column_index < rem_columns:
				index = rem_rows - 1
				while index >= row_index:
					if self.board[index][column_index]:
						board_list.append(self.board[index][column_index])
					index -= 1
				column_index += 1
		return board_list

	def count_inversions(self):
		board_1d = self.board_spiral_translate()
		index = 0
		inversions = 0
		while index < len(board_1d) - 1:
			j_index = index + 1
			while j_index < len(board_1d):
				if board_1d[index] > board_1d[j_index]:
					inversions += 1
				j_index += 1
			index += 1
		return inversions

	def is_solvable(self):
		inversions = self.count_inversions()
		if inversions % 2 == 0:
			return True
		else:
			return False

	def generate_goal_board(self):
		goal = deepcopy(self.board)
		row_index = 0
		rem_rows = self.size
		column_index = 0
		rem_columns = self.size
		cell = 1
		while row_index < rem_rows and column_index < rem_columns:
			index = column_index
			while index < rem_columns:
				if cell != (self.size)**2:
					goal[row_index][index] = cell
				else:
					goal[row_index][index] = 0
				cell += 1
				index += 1
			row_index += 1
			index = row_index
			while index < rem_rows:
				if cell != (self.size)**2:
					goal[index][rem_columns - 1] = cell
				else:
					goal[index][rem_columns - 1] = 0
				cell += 1
				index += 1
			rem_columns -= 1
			if row_index < rem_rows:
				index = rem_columns - 1
				while index >= column_index:
					if cell != (self.size)**2:
						goal[rem_rows - 1][index] = cell
					else:
						goal[rem_rows - 1][index] = 0
					cell += 1
					index -= 1
				rem_rows -= 1
			if column_index < rem_columns:
				index = rem_rows - 1
				while index >= row_index:
					if cell != (self.size)**2:
						goal[index][column_index] = cell
					else:
						goal[index][column_index] = 0
					cell += 1
					index -= 1
				column_index += 1
		return goal

	def goal_state(self):
		if not self.goal_board:
			self.goal_board = Board(self.generate_goal_board())
		return self.goal_board

	def equals(self, board):
		if self.board == board.board:
			return True
		else:
			return False

	def is_goal_state(self):
		if self.equals(self.goal_state()):
			return True
		else:
			return False
