from npuzzle_mod import Board

npuzzle = []
npuzzle.append([1, 5, 7])
npuzzle.append([2, 0, 6])
npuzzle.append([3, 8, 4])

board = Board(npuzzle)

print("npuzzle: {}, inversions: {}".format(board, board.count_inversions()))

npuzzle1 = []
npuzzle1.append([1, 2, 3])
npuzzle1.append([8, 0, 4])
npuzzle1.append([7, 6, 5])

board1 = Board(npuzzle1)

print("npuzzle1: {}, inversions: {}".format(board1, board1.count_inversions()))
