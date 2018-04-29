from state import State
from validator import Validator
import goal
import move
import heapq
import sys

def is_goal_state(board, goal):
	if board == goal:
		return True
	else:
		return False

def display_state(state, step):
	
	size = len(state)
	print '                             Move: {}'.format(step)
	print '         _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _\n'
	for i in range(size):
		for j in range(size):
			sys.stdout.write('\t|\t')
			if state[i][j] == 0:
				sys.stdout.write(' ')
			else:
				sys.stdout.write(str(state[i][j]))
		print '\t|\t '
		print '         _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _\n'
	print '\n'

def display_path(x):
	stack = []
	stack.append(x)
	steps = -1
	while x.parent :
		x = x.parent
		stack.append(x)
	while stack:
		steps += 1
		state = stack.pop().board
		display_state(state, steps)
	print 'Moves: {}'.format(steps)

def sovle_puzzle(start_board, hc):

	openset = []
	closed = []
	complexity_in_time = 1
	size = len(start_board)
	goal_state = goal_state = goal.generate_goal(size)
	start = State(start_board, goal_state, None, hc)

	if is_goal_state(start.board, goal_state):
		print 'Puzzle is already in Goal State'
		return
	
	move.possible_moves(start, openset, closed, goal_state, hc)
	opsize = len(openset)
	for i in range(opsize):
		print openset[i][0]
		print openset[i][1].board
	closed.append(start.board)

	while openset:
		x = heapq.heappop(openset)[1]
		complexity_in_time += 1
		if is_goal_state(x.board, goal_state):
			display_path(x)
			print 'Complexity In Time: {}'.format(complexity_in_time)
			break
		closed.append(x.board)
		move.possible_moves(x, openset, closed, goal_state, hc)
		opsize = len(openset)
		for i in range(opsize):
			print openset[i][0]
			print openset[i][1].board
	print 'Complexity In Size: {}'.format(len(closed) + len(openset))

def main():

	print("start main")

	heuristics = ["manhattan", "hamming", "row_and_column"]

	if (len(sys.argv) == 2) and (sys.argv[1] in heuristics):
		validate = Validator()
		start_board = validate.build_npuzzle()
		print(start_board)
		print("validation done")
		if not start_board:
			print("Error")
		chosen_heuristic = heuristics.index(sys.argv[1]) + 1
		print(chosen_heuristic)
		sovle_puzzle(start_board, chosen_heuristic)
	else:
		print("Error")
		print("Usage: main.py heuristic < puzzle.txt")
		print("heuristic = manhattan OR hamming OR row_and_column")

if __name__ == "__main__":
	main()
