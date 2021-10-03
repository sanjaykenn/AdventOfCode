import functools
import operator
from collections import deque

import graph


def main(inp):
	def knot_hash(value):
		lengths = list(map(ord, value)) + [17, 31, 73, 47, 23]

		numbers = deque(range(256))
		position = 0
		skip_size = 0

		for _ in range(64):
			for length in lengths:
				numbers.rotate(-position)
				numbers = list(numbers)
				numbers[:length] = list(reversed(numbers[:length]))
				numbers = deque(numbers)
				numbers.rotate(position)

				position = (position + length + skip_size) % len(numbers)
				skip_size += 1

		numbers = list(numbers)

		dense = []
		for block in range(0, 256, 16):
			dense.append(functools.reduce(operator.xor, numbers[block:block + 16]))

		return ''.join(map('{:02x}'.format, dense))

	size = 128
	inp = inp.rstrip('\n')

	field = list(map(
		lambda i: f'{{:0{size}b}}'.format(int(knot_hash(f'{inp}-{i}'), 16)),
		range(size)
	))

	g = graph.Graph()
	for y in range(size):
		for x in range(size):
			if field[y][x] != '1':
				continue

			g.add_node((x, y))
			for x1, y1 in ((x + 1, y), (x, y + 1)):
				if y1 < size and x1 < size and field[y1][x1] == '1':
					g.add_edge((x, y), (x1, y1), bidirectional=True)

	return len(g.components())


if __name__ == '__main__':
	import sys
	print(main(''.join(sys.stdin.readlines())))
