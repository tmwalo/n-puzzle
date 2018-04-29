# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    main.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: tmwalo <marvin@42.fr>                      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/04/29 09:22:56 by tmwalo            #+#    #+#              #
#    Updated: 2018/04/29 11:34:52 by tmwalo           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from npuzzle_mod import Board
from validator import Validator
from helpers import generate_random_board
import solve_puzzle
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
		solve_puzzle.sovle_puzzle(start_board.board, heuristic_key)
	else:
		sys.stderr.write("Puzzle can not be solved\n")
                solve_puzzle.display_state(start_board.board, 0)
elif validation_error:
	sys.stderr.write("Error\n")
elif usage_error:
	sys.stderr.write("Error\nUsage: main.py -f|-r heuristic npuzzle.txt|random_puzzle_size\nheuristic = manhattan OR hamming OR row_and_column\n")
