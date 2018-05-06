from npuzzle_mod import Board

npuzzle = []
npuzzle.append([1, 5, 7])
npuzzle.append([2, 0, 6])
npuzzle.append([3, 8, 4])

board = Board(npuzzle)
print("npuzzle: {}".format(board.board))
possible_moves = board.possible_moves()
for coords in possible_moves:
	print("x - {}, y - {}".format(coords["x"], coords["y"]))

npuzzle1 = []
npuzzle1.append([1, 5, 0])
npuzzle1.append([2, 7, 6])
npuzzle1.append([3, 8, 4])

board1 = Board(npuzzle1)
print("npuzzle: {}".format(board1.board))
possible_moves1 = board1.possible_moves()
for coords in possible_moves1:
	print("x - {}, y - {}".format(coords["x"], coords["y"]))
