import helpers
import random

print(helpers.generate_random_array(3))
if not helpers.generate_random_array(-3):
	print("PASS")
print(helpers.generate_random_array(6))
print(helpers.generate_random_array(4))
