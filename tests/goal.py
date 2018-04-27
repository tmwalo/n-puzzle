from npuzzle_mod import Board

npuzzle = []
npuzzle.append([2, 1, 5])
npuzzle.append([8, 6, 4])
npuzzle.append([7, 0, 3])

board = Board(npuzzle)
goal = board.goal_state()

print("npuzzle: {}".format(npuzzle))
print("goal state: {}".format(goal.board))
