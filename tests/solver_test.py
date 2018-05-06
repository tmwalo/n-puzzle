from npuzzle_mod import Board
from solver import Solver

npuzzle = []
npuzzle.append([2, 0, 6])
npuzzle.append([1, 4, 3])
npuzzle.append([8, 7, 5])

board = Board(npuzzle)

print("npuzzle: {}".format(board.board))

solver = Solver(board, "manhattan")
solver.solve()
