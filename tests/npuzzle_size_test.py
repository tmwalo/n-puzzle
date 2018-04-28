from validator import Validator

validate = Validator()

if not validate.npuzzle_size(333):
	print("PASS")
else:
	print("FAIL")

if not validate.npuzzle_size(3.33):
	print("PASS")
else:
	print("FAIL")

if not validate.npuzzle_size(True):
	print("PASS")
else:
	print("FAIL")

if not validate.npuzzle_size("311cats"):
	print("PASS")
else:
	print("FAIL")

if not validate.npuzzle_size(""):
	print("PASS")
else:
	print("FAIL")

if validate.npuzzle_size("27"):
	print("PASS")
else:
	print("FAIL")

if validate.npuzzle_size("187 #comment"):
	print("PASS")
else:
	print("FAIL")

if not validate.npuzzle_size("2"):
	print("PASS")
else:
	print("FAIL")

if validate.npuzzle_size("	 27		    	"):
	print("PASS")
else:
	print("FAIL")

if validate.npuzzle_size(" 187		 #comment    "):
	print("PASS")
else:
	print("FAIL")

if not validate.npuzzle_size("	   	 	    	  	 	  "):
	print("PASS")
else:
	print("FAIL")
