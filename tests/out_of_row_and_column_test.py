from npuzzle_mod import Board

npuzzle = []
npuzzle.append([2, 0, 5])
npuzzle.append([8, 1, 4])
npuzzle.append([7, 6, 3])

board = Board(npuzzle)
goal = board.goal_state()

print("npuzzle: {}".format(npuzzle))
print("goal state: {}".format(goal.board))
print("out of row and column: {}".format(board.out_of_row_and_column()))
