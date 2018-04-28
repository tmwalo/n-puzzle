# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    npuzzle_mod.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: tmwalo <marvin@42.fr>                      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/01/30 15:13:29 by tmwalo            #+#    #+#              #
#    Updated: 2018/04/28 11:01:06 by tmwalo           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from copy import deepcopy

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

	def hamming_distance(self):
		index = 1
		heuristic = 0
		while index < (self.get_size())**2:
			if self.cell_manhattan_dist(index):
				heuristic += 1
			index += 1
		return heuristic

	def cell_out_of_row_and_column(self, value):
		board_coord = self.coordinates(value)
		goal_coord = (self.goal_state()).coordinates(value)
		out_of_row_and_column = 0
		if (board_coord["x"] - goal_coord["x"]):
			out_of_row_and_column += 1
		if (board_coord["y"] - goal_coord["y"]):
			out_of_row_and_column += 1
		return out_of_row_and_column

	def out_of_row_and_column(self):
		index = 1
		heuristic = 0
		while index < (self.get_size())**2:
			heuristic += self.cell_out_of_row_and_column(index)
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
