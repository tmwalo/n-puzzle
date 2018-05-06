from npuzzle_mod import Board
import heapq

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

	def is_goal_reached(self, cmp_board):
		if self.get_goal_board().board == cmp_board.board:
			return True
		else:
			return False

	def solve(self):
		open_set = []
		self.get_start_board().set_h_score(self.get_heuristic())
		self.get_start_board().set_f_score(self.get_start_board().get_g_score() + self.get_start_board().get_h_score())
		heapq.heappush(open_set, (self.get_start_board().get_f_score(), self.get_start_board()))
		closed_set = []
		success = False
		while open_set and (not success):
			selected_board = heapq.heappop(open_set)[1]
			if self.is_goal_reached(selected_board):
				success = True
			else:
				children = selected_board.generate_children()
				child_g_score = selected_board.get_g_score() + self.get_cost_per_move()
				for child in children:
					if (child not in open_set) and (child not in closed_set):
						child.set_g_score(child_g_score)
						child.set_h_score(self.get_heuristic())
						child.set_f_score(child.get_g_score() + child.get_h_score())
						child.set_parent(selected_board)
						heapq.heappush(open_set, (child.get_f_score(), child))
					else:
						if child in open_set:
							duplicate_board_index = open_set.index(child)
							duplicate_board = open_set[duplicate_board_index]
							if child_g_score < duplicate_board.get_g_score():
								duplicate_board.set_g_score(child_g_score)
								duplicate_board.set_f_score(duplicate_board.get_g_score() + duplicate_board.get_h_score())
								duplicate_board.set_parent(selected_board)
						else:
							duplicate_board_index = closed_set.index(child)
							duplicate_board = closed_set[duplicate_board_index]
							if child_g_score < duplicate_board.get_g_score():
								duplicate_board = closed_set.pop(duplicate_board_index)
								duplicate_board.set_g_score(child_g_score)
								duplicate_board.set_f_score(duplicate_board.get_g_score() + duplicate_board.get_h_score())
								duplicate_board.set_parent(selected_board)
								heapq.heappush(open_set, (duplicate_board.get_f_score(), duplicate_board))
				closed_set.append(selected_board)
		if success:
			print(selected_board.board)
