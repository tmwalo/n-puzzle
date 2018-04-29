# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    helpers.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: tmwalo <marvin@42.fr>                      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/04/29 09:22:28 by tmwalo            #+#    #+#              #
#    Updated: 2018/04/29 09:22:48 by tmwalo           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

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

def generate_random_board(size):
	if size < 3:
		return None
	board = []
	board_1d = generate_random_array(size)
	index = 0
	row = 0
	while row < size:
		column = 0
		board_row = []
		while column < size:
			board_row.append(board_1d[index])
			index += 1
			column += 1
		board.append(board_row)
		row += 1
	return board
