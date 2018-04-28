import helpers
import random

print(helpers.generate_random_board(3))
if not helpers.generate_random_board(-3):
	print("PASS")
print(helpers.generate_random_board(6))
print(helpers.generate_random_board(4))
