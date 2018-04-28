from validator import Validator

validate = Validator()

print(validate.store_npuzzle_size(13))

print(validate.store_npuzzle_size("	  	 	 	   "))

print(validate.store_npuzzle_size("13"))

print(validate.store_npuzzle_size("13 #comment"))

print(validate.store_npuzzle_size(" 	 13	 #comment	 	"))
