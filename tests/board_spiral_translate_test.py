from npuzzle_mod import Board

npuzzle = []
npuzzle.append([1, 2, 3])
npuzzle.append([8, 0, 4])
npuzzle.append([7, 6, 5])

board = Board(npuzzle)

print(board.board_spiral_translate())
