from npuzzle_mod import is_comment

if not is_comment(777):
	print("PASS")
else:
	print("FAIL")

if not is_comment(7.77):
	print("PASS")
else:
	print("FAIL")

if not is_comment(False):
	print("PASS")
else:
	print("FAIL")

if is_comment("#comment"):
	print("PASS")
else:
	print("FAIL")

if not is_comment(""):
	print("PASS")
else:
	print("FAIL")

if not is_comment("not comment"):
	print("PASS")
else:
	print("FAIL")

if is_comment("# comment"):
	print("PASS")
else:
	print("FAIL")

if not is_comment("	 not  		comment	 "):
	print("PASS")
else:
	print("FAIL")

if is_comment("	 # 		comment	"):
	print("PASS")
else:
	print("FAIL")

if is_comment("  		#comment	 	 "):
	print("PASS")
else:
	print("FAIL")

if not is_comment("  			 	 	 "):
	print("PASS")
else:
	print("FAIL")
