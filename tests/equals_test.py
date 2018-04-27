from npuzzle_mod import Board

npuzzle1 = []
npuzzle1.append([1, 2, 3])
npuzzle1.append([8, 0, 4])
npuzzle1.append([7, 6, 5])

board1 = Board(npuzzle1)

npuzzle2 = []
npuzzle2.append([1, 2, 3])
npuzzle2.append([8, 0, 4])
npuzzle2.append([7, 6, 5])

board2 = Board(npuzzle2)

npuzzle3 = []
npuzzle3.append([8, 2, 5])
npuzzle3.append([3, 7, 4])
npuzzle3.append([0, 6, 1])

board3 = Board(npuzzle3)

print("board1: {}".format(board1.board))
print("board2: {}".format(board2.board))
print("board3: {}".format(board3.board))

print("board1 equals board2: {}".format(board1.equals(board2)))
print("board2 equals board1: {}".format(board2.equals(board1)))
print("board1 equals board3: {}".format(board1.equals(board3)))
