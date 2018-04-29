# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    main.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: tmwalo <marvin@42.fr>                      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/04/29 09:22:56 by tmwalo            #+#    #+#              #
#    Updated: 2018/04/29 09:23:10 by tmwalo           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from npuzzle_mod import Board
from validator import Validator
from helpers import generate_random_board
import sys

heuristics = ["manhattan", "hamming", "row_and_column"]
usage_error = False
validation_error = False

if len(sys.argv) == 4:
	if sys.argv[1] == "-f":
		validate = Validator()
		start_board_array = validate.build_npuzzle(sys.argv[3])
		if not start_board_array:
			validation_error = True
	elif sys.argv[1] == "-r":
		try:
			board_size = int(sys.argv[3])
			start_board_array = generate_random_board(board_size)
		except ValueError:
			board_size = None
			start_board_array = None
		if not start_board_array:
			validation_error = True
	else:
		usage_error = True
	if sys.argv[2] in heuristics:
		heuristic_key = heuristics.index(sys.argv[2]) + 1
	elif not usage_error:
		usage_error = True
else:
	usage_error = True

if (not usage_error) and (not validation_error):
	start_board = Board(start_board_array)
	if start_board.is_solvable():
		# CALL PUZZLE SOLVER(with heuristic key)
		print("call solver")
	else:
		print("Puzzle can not be solved")
elif validation_error:
	print("Error")
elif usage_error:
	print("Error\nUsage: main.py -f|-r heuristic npuzzle.txt|random_puzzle_size")
