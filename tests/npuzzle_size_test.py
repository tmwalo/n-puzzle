from npuzzle_mod import npuzzle_size

if not npuzzle_size(333):
	print("PASS")
else:
	print("FAIL")

if not npuzzle_size(3.33):
	print("PASS")
else:
	print("FAIL")

if not npuzzle_size(True):
	print("PASS")
else:
	print("FAIL")

if not npuzzle_size("311cats"):
	print("PASS")
else:
	print("FAIL")

if not npuzzle_size(""):
	print("PASS")
else:
	print("FAIL")

if npuzzle_size("27"):
	print("PASS")
else:
	print("FAIL")

if npuzzle_size("187 #comment"):
	print("PASS")
else:
	print("FAIL")

if not npuzzle_size("2"):
	print("PASS")
else:
	print("FAIL")

if npuzzle_size("	 27		    	"):
	print("PASS")
else:
	print("FAIL")

if npuzzle_size(" 187		 #comment    "):
	print("PASS")
else:
	print("FAIL")

if not npuzzle_size("	   	 	    	  	 	  "):
	print("PASS")
else:
	print("FAIL")
