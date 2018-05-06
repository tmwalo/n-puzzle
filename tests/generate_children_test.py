from npuzzle_mod import Board

npuzzle = []
npuzzle.append([1, 5, 7])
npuzzle.append([2, 0, 6])
npuzzle.append([3, 8, 4])

board = Board(npuzzle)

print("npuzzle: {}".format(board.board))

children = board.generate_children()

for child in children:
	print(child.board)
