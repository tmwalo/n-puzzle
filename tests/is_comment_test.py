from validator import Validator

validate = Validator()

if not validate.is_comment(777):
	print("PASS")
else:
	print("FAIL")

if not validate.is_comment(7.77):
	print("PASS")
else:
	print("FAIL")

if not validate.is_comment(False):
	print("PASS")
else:
	print("FAIL")

if validate.is_comment("#comment"):
	print("PASS")
else:
	print("FAIL")

if not validate.is_comment(""):
	print("PASS")
else:
	print("FAIL")

if not validate.is_comment("not comment"):
	print("PASS")
else:
	print("FAIL")

if validate.is_comment("# comment"):
	print("PASS")
else:
	print("FAIL")

if not validate.is_comment("	 not  		comment	 "):
	print("PASS")
else:
	print("FAIL")

if validate.is_comment("	 # 		comment	"):
	print("PASS")
else:
	print("FAIL")

if validate.is_comment("  		#comment	 	 "):
	print("PASS")
else:
	print("FAIL")

if not validate.is_comment("  			 	 	 "):
	print("PASS")
else:
	print("FAIL")
