import itertools


def main(inp):
	n = int(inp)

	def is_space(x, y):
		return bin(x*x + 3*x + 2*x*y + y + y*y + n).count('1') & 1 == 0

	positions = {(1, 1)}
	visited = set()
	for step in itertools.count():
		if (31, 39) in positions:
			return step

		visited |= positions
		new_positions = set()
		for x, y in positions:
			for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
				x1 = x + dx
				y1 = y + dy
				if is_space(x1, y1) and (x1, y1) not in visited:
					new_positions.add((x1, y1))

		positions = new_positions


if __name__ == '__main__':
	import sys
	print(main(''.join(sys.stdin.readlines())))
