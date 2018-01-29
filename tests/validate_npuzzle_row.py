from npuzzle_mod import validate_npuzzle_row

if not validate_npuzzle_row("4 6 8", 1):
	print("PASS")
else:
	print("FAIL")

if not validate_npuzzle_row("-4	-11 -6", 3):
	print("PASS")
else:
	print("FAIL")

if not validate_npuzzle_row("7", 3):
	print("PASS")
else:
	print("FAIL")

if not validate_npuzzle_row("5 6 1 0 8 11", 4):
	print("PASS")
else:
	print("FAIL")

if not validate_npuzzle_row("5 1000 23", 3):
	print("PASS")
else:
	print("FAIL")

if validate_npuzzle_row("9 7 4 11", 4):
	print("PASS")
else:
	print("FAIL")

if validate_npuzzle_row(" 	9	7  	4	 11  	", 4):
	print("PASS")
else:
	print("FAIL")

if validate_npuzzle_row("9 7 4 11 #comment", 4):
	print("PASS")
else:
	print("FAIL")

if validate_npuzzle_row(" 	9	7  	4	 11  	#comment 	", 4):
	print("PASS")
else:
	print("FAIL")
