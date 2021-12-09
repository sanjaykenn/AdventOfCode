from collections import deque

import numpy as np


def get_neighbors(x, y, a):
	for x1, y1 in [(x, y - 1), (x - 1, y), (x + 1, y), (x, y + 1)]:
		if 0 <= y1 < len(a) and 0 <= x1 < len(a[y]):
			yield x1, y1


def find_basin(x, y, a, free):
	if a[y, x] >= 9 or not free[y, x]:
		return 0

	coords = {(x, y)}
	size = 0
	free[y, x] = False

	while coords:
		new_coords = set()
		for x1, y1 in coords:
			new_coords |= {(x2, y2) for x2, y2 in get_neighbors(x1, y1, a) if free[y2, x2] and a[y2, x2] < 9}

		for x1, y1 in new_coords:
			free[y1, x1] = False

		size += len(coords)
		coords = new_coords

	return size


def main(inp):
	a = np.array([list(line) for line in inp.splitlines()], int)
	free = np.ones_like(a, bool)
	sizes = deque()

	for y in range(len(a)):
		for x in range(len(a[y])):
			size = find_basin(x, y, a, free)
			if size > 0:
				sizes.append(size)

	return np.prod(sorted(sizes, reverse=True)[:3])


if __name__ == '__main__':
	import sys
	print(main(''.join(sys.stdin.readlines())))
