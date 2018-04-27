from npuzzle_mod import Board

npuzzle1 = []
npuzzle1.append([1, 2, 3])
npuzzle1.append([8, 0, 4])
npuzzle1.append([7, 6, 5])

board1 = Board(npuzzle1)

npuzzle2 = []
npuzzle2.append([8, 2, 5])
npuzzle2.append([3, 7, 4])
npuzzle2.append([0, 6, 1])

board2 = Board(npuzzle2)

print("board1: {}".format(board1.board))
print("board2: {}".format(board2.board))

print("board1 is goal state: {}".format(board1.is_goal_state()))
print("board2 is goal state: {}".format(board2.is_goal_state()))
