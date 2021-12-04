import numpy as np


class Board:
	def __init__(self, board):
		self.board = board
		self.last_number = None
		self.is_marked = np.zeros_like(board, dtype=bool)

	def mark_number(self, n):
		self.is_marked[self.board == n] = True
		self.last_number = n

	def is_solved(self):
		for row in self.is_marked:
			if row.all():
				return self.get_score()

		for col in self.is_marked.transpose():
			if col.all():
				return self.get_score()

	def get_score(self):
		return np.sum(self.board[np.invert(self.is_marked)]) * self.last_number


def main(inp):
	inp = inp.rstrip('\n').split('\n\n')
	numbers = map(int, inp[0].split(','))
	boards = []
	last_score = None

	for b in inp[1:]:
		board = np.array([list(map(int, row.split())) for row in b.splitlines()])
		boards.append(Board(board))

	for n in numbers:
		new_boards = []

		for board in boards:
			board.mark_number(n)
			score = board.is_solved()

			if score is not None:
				last_score = score
			else:
				new_boards.append(board)

		boards = new_boards

	return last_score


if __name__ == '__main__':
	import sys
	print(main(''.join(sys.stdin.readlines())))
