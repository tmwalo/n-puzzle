from npuzzle_mod import Board

npuzzle = []
npuzzle.append([1, 5, 7])
npuzzle.append([2, 0, 6])
npuzzle.append([3, 8, 4])

board = Board(npuzzle)

print("npuzzle: {}".format(board.board))

zero_coords = board.coordinates(0)
possible_moves = board.possible_moves()
board.swap_cells(zero_coords, possible_moves[0])

print("npuzzle after swap: {}".format(board.board))
