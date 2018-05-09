from npuzzle_mod import Board
import heapq
import time

class Solver:

	def __init__(self, start_board, heuristic):
		self.start_board = start_board
		self.goal_board = None
		self.heuristic = heuristic
		self.cost_per_move = 1

	def get_cost_per_move(self):
		return self.cost_per_move

	def get_goal_board(self):
		if not self.goal_board:
			self.goal_board = self.get_start_board().goal_state()
		return self.goal_board

	def get_start_board(self):
		return self.start_board

	def get_heuristic(self):
		return self.heuristic

	def get_path(self, board):
		path = []
		current_board = board
		while current_board.get_parent():
			path.append(current_board)
			current_board = current_board.get_parent()
		path.append(self.get_start_board())
		while path:
			state = path.pop()
#			print("\nmove: {}\n{}".format(state.get_g_score(), state.print_board()))

	def is_goal_reached(self, cmp_board):
		if self.get_goal_board().board == cmp_board.board:
			return True
		else:
			return False

	def set_child_state(self, child, parent):
		child_g_score = parent.get_g_score() + self.get_cost_per_move()
		child.set_g_score(child_g_score)
		child.set_h_score(self.get_heuristic())
		child.set_f_score(child.get_g_score() + child.get_h_score())
		child.set_parent(parent)

	def solve(self):
		start = time.time()
		open_set = []
		search_open_set = set()
		self.get_start_board().set_h_score(self.get_heuristic())
		self.get_start_board().set_f_score(self.get_start_board().get_g_score() + self.get_start_board().get_h_score())
		heapq.heappush(open_set, (self.get_start_board().get_f_score(), self.get_start_board()))
		search_open_set.add(self.get_start_board())
		closed_set = set()
		success = False
		count = 1
		while open_set and (not success) and (count < 6):
			print("OPEN SET:")
			for board in open_set:
				board[1].print_board()
				print()
			selected_board = heapq.heappop(open_set)[1]
			print("SELECTED BOARD:")
			selected_board.print_board()
			print()
			search_open_set.discard(selected_board)
			if self.is_goal_reached(selected_board):
				success = True
			else:
				children = selected_board.generate_children()
				for child in children:
					self.set_child_state(child, selected_board)
					if child in search_open_set:
						duplicate_board_index = open_set.index(child)
						duplicate_board = open_set[duplicate_board_index]
						if child.get_f_score() < duplicate_board.get_f_score():
							self.set_child_state(duplicate_board, selected_board)
					elif child in closed_set:
						for board in closed_set:
							if child.equals(board):
								duplicate_board = board
								break
						if child.get_f_score() < duplicate_board.get_f_score():
							closed_set.discard(duplicate_board)
							heapq.heappush(open_set, (child.get_f_score(), child))
							search_open_set.add(child)
					else:
						heapq.heappush(open_set, (child.get_f_score(), child))
						search_open_set.add(child)
				closed_set.add(selected_board)
				print("CLOSED SET:")
				for board in closed_set:
					board.print_board()
					print()
				count += 1
		if success:
			self.get_path(selected_board)
			print("running time: {} seconds".format(time.time() - start))
