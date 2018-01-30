import npuzzle_mod

board = []
board.append([1, 5, 7])
board.append([2, 0, 6])
board.append([3, 8, 4])

print("npuzzle: {}, inversions: {}".format(board, npuzzle_mod.count_inversions(board, 3)))

board1 = []
board1.append([1, 2, 3])
board1.append([8, 0, 4])
board1.append([7, 6, 5])

print("npuzzle: {}, inversions: {}".format(board1, npuzzle_mod.count_inversions(board1, 3)))
