import npuzzle_mod

npuzzle = npuzzle_mod.build_npuzzle()
board = npuzzle_mod.Board(npuzzle)
print("board: {}\nsolvable: {}".format(board, board.is_solvable()))

