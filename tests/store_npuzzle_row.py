from validator import Validator

validate = Validator()

print(validate.store_npuzzle_row("9 7 4 11", 4))

print(validate.store_npuzzle_row(" 	9	7  	4	 11  	", 4))

print(validate.store_npuzzle_row("9 7 4 11 #comment", 4))

print(validate.store_npuzzle_row(" 	9	7  	4	 11  	#comment 	", 4))
