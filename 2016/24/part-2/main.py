import itertools

import graph


def main(inp):
	field = [list(line) for line in inp.rstrip('\n').split('\n')]

	def get_lengths(x1, y1):
		coordinates = {(x1, y1)}
		visited = set()

		for i in itertools.count():
			if i > 0:
				for x, y in coordinates:
					if field[y][x].isnumeric():
						yield field[y][x], i

			visited |= coordinates
			new_coordinates = set()

			for x, y in coordinates:
				for nx, ny in ((x, y - 1), (x - 1, y), (x + 1, y), (x, y + 1)):
					if 0 <= ny < len(field) and 0 <= nx < len(field[ny]) and field[ny][nx] != '#' and (nx, ny) not in visited:
						new_coordinates.add((nx, ny))

			if not new_coordinates:
				break

			coordinates = new_coordinates

	nodes = set()
	for y in range(len(field)):
		for x in range(len(field[y])):
			if field[y][x].isnumeric():
				nodes.add((field[y][x], (x, y)))

	g = graph.Graph()
	for v1, (x1, y1) in nodes:
		for v2, d in get_lengths(x1, y1):
			g.add_edge(v1, v2, d, True)

	return g.solve_tsp(method='bnb')[0]


if __name__ == '__main__':
	import sys
	print(main(''.join(sys.stdin.readlines())))
