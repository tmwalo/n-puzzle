from npuzzle_mod import Board

npuzzle = []
npuzzle.append([1, 2, 3])
npuzzle.append([0, 8, 4])
npuzzle.append([7, 6, 5])

board = Board(npuzzle)

print("npuzzle: {}".format(board.board))

children = board.generate_children()

for child in children:
	print(child.board)
