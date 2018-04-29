import itertools
import sys

def generate_goal(size):
	
	goal = [ [0] * size for row in range(size)]
	n = itertools.count(1)
	
	r = list(range(size))
	c = list(range(size))
	max_val = size * size
	while r or c:
		if r:
			i = r.pop(0)
			for j in c:
				val = n.__next__()
				if val == max_val:
					goal[i][j] = 0
				else:
					goal[i][j] = val			

		if c:
			j = c.pop(-1)
			for i in r:
				val = n.__next__()
				if val == max_val:
					goal[i][j] = 0
				else:
					goal[i][j] = val
		if r:
			i = r.pop(-1)
			for j in reversed(c):
				val = n.__next__()
				if val == max_val:
					goal[i][j] = 0
				else:
					goal[i][j] = val

		if c:
			j = c.pop(0)
			for i in reversed(r):
				val = n.__next__()
				if val == max_val:
					goal[i][j] = 0
				else:
					goal[i][j] = val

	print(goal)
