from validator import Validator

validate = Validator()

board = []
board.append([1, 5, 7])
board.append([2, 2, 6])
board.append([3, 8, 4])
if not validate.validate_sequence(board, 3):
	print("PASS")
else:
	print("FAIL")

board1 = []
board1.append([1, 5, 7])
board1.append([2, 0, 6])
board1.append([3, 12, 4])
if not validate.validate_sequence(board1, 3):
	print("PASS")
else:
	print("FAIL")

board2 = []
board2.append([1, 5, 7])
board2.append([2, 9, 6])
board2.append([3, 8, 4])
if not validate.validate_sequence(board2, 3):
	print("PASS")
else:
	print("FAIL")

board3 = []
board3.append([1, 5, 7])
board3.append([2, 0, 6])
board3.append([3, 8, 4])
if validate.validate_sequence(board3, 3):
	print("PASS")
else:
	print("FAIL")
