import npuzzle_mod
from npuzzle_mod import Board

npuzzle = []
npuzzle.append([1, 5, 7])
npuzzle.append([2, 0, 6])
npuzzle.append([3, 8, 4])

board = Board(npuzzle.board)

print("board: {}\nsolvable: {}".format(board, board.is_solvable()))

