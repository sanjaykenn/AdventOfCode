import itertools
import re
from collections import deque

import getkey


class Node:
	def __init__(self, used, size):
		self.used = used
		self.size = size

	def is_pair(self, node_b):
		return 0 < self.used <= node_b.size - node_b.used

	def copy(self):
		return Node(self.used, self.size)

	def __repr__(self):
		return f'Node({self.used}, {self.size})'


class StorageGrid:
	def __init__(self, nodes, target=None, cursor=None, path=None):
		self.width = len(nodes[0])
		self.height = len(nodes)
		self.nodes = nodes
		self.target = target or (self.width - 1, 0)
		self.cursor = cursor or StorageGrid.find_cursor(nodes)
		self.path = deque(path or [self.cursor])

	def get_possible_moves(self):
		x, y = self.cursor
		for x1, y1 in ((x, y - 1), (x - 1, y), (x + 1, y), (x, y + 1)):
			if 0 <= x1 < self.width and 0 <= y1 < self.height:
				yield x1, y1

	def move_to_cursor(self, x, y):
		if len(self.path) >= 2 and self.path[-2] == (x, y):
			return False

		if (x, y) == self.target:
			self.target = self.cursor

		self.cursor = x, y
		self.path.append((x, y))

		return True

	def copy(self):
		return StorageGrid(self.nodes, self.target, self.cursor, self.path)

	def is_solved(self):
		return self.target == (0, 0)

	@staticmethod
	def find_cursor(nodes):
		for y in range(len(nodes)):
			for x in range(len(nodes[y])):
				for x1, y1 in ((x, y - 1), (x - 1, y), (x + 1, y), (x, y + 1)):
					if 0 <= x1 < len(nodes[y]) and 0 <= y1 < len(nodes) and nodes[y][x].is_pair(nodes[y1][x1]):
						return x1, y1


def main(inp):
	re_node = re.compile('^/dev/grid/node-x(\\d+)-y(\\d+) +(\\d+)T +(\\d+)T +\\d+T +\\d+%$')

	inp = list(map(lambda line: tuple(map(int, re_node.match(line).groups())), inp.rstrip('\n').split('\n')[2:]))
	nodes = []
	for x, y, size, used in inp:
		if y >= len(nodes):
			nodes.append([])

		nodes[y].append(Node(used, size))

	start = 0, 0
	goal = len(nodes[0]) - 1, 0

	for i in itertools.count():
		print('Steps:', i)
		cursor = None
		for y in range(len(nodes)):
			for x in range(len(nodes[y])):
				if (x, y) == goal:
					print('G', end='')
				elif nodes[y][x].used == 0:
					print('_', end='')
					cursor = x, y
				else:
					print('.', end='')

			print()

		if start == goal:
			return

		while True:
			k = getkey.getkey()

			if k == getkey.keys.UP:
				x1, y1 = cursor[0], cursor[1] - 1
			elif k == getkey.keys.DOWN:
				x1, y1 = cursor[0], cursor[1] + 1
			elif k == getkey.keys.LEFT:
				x1, y1 = cursor[0] - 1, cursor[1]
			elif k == getkey.keys.RIGHT:
				x1, y1 = cursor[0] + 1, cursor[1]
			else:
				continue

			if 0 <= y1 < len(nodes) and 0 <= x1 < len(nodes[y1]) and nodes[y1][x1].is_pair(nodes[cursor[1]][cursor[0]]):
				nodes[cursor[1]][cursor[0]].used += nodes[y1][x1].used
				nodes[y1][x1].used = 0
				if (x1, y1) == goal:
					goal = cursor

				break

		print(f'\x1b[{len(nodes) + 1}A', end='')


if __name__ == '__main__':
	with open('input.txt') as f:
		main(f.read())
