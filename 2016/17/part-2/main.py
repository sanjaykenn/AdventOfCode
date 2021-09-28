import hashlib
import itertools
from collections import deque


class State:
	PREFIX = ''
	SIZE = 4

	def __init__(self, x, y, path=None):
		self.x = x
		self.y = y
		self.path = path or deque()

	def get_next_states(self):
		if self.is_solved():
			return []

		h = hashlib.md5(f'{State.PREFIX}{"".join(self.path)}'.encode()).hexdigest()
		result = deque()
		if self.y > 0 and int(h[0], 16) > 10:
			result.append(State(self.x, self.y - 1, self.path + deque(['U'])))

		if self.y < State.SIZE - 1 and int(h[1], 16) > 10:
			result.append(State(self.x, self.y + 1, self.path + deque(['D'])))

		if self.x > 0 and int(h[2], 16) > 10:
			result.append(State(self.x - 1, self.y, self.path + deque(['L'])))

		if self.x < State.SIZE - 1 and int(h[3], 16) > 10:
			result.append(State(self.x + 1, self.y, self.path + deque(['R'])))

		return result

	def is_solved(self):
		return self.x == self.y == State.SIZE - 1


def main(inp):
	State.PREFIX = inp.rstrip('\n')

	states = deque([State(0, 0)])
	result = 0
	for steps in itertools.count():
		if any(map(State.is_solved, states)):
			result = steps
		elif not states:
			return result

		new_states = deque()

		for state in states:
			new_states.extend(state.get_next_states())

		states = new_states


if __name__ == '__main__':
	import sys
	print(main(''.join(sys.stdin.readlines())))
