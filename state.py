import heuristics

class State:

	def __init__(self, board, goal, parent, hc):
		self.board = board
		self.size = len(board)
		self.parent = parent
		print parent
		self.h = heuristics.heuristic(board, goal, self.size, hc)
		print 'H---: {}'.format(self.h)
		self.g = heuristics.get_depth(parent)
		print 'G---: {}'.format(self.g)
		self.f = self.g + self.h
		print 'F---: {}'.format(self.f)
