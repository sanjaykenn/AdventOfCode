import numpy as np


def main(inp):
	a = np.array([list(map(int, line)) for line in inp.splitlines()])
	flashes = 0

	for _ in range(100):
		a += 1
		flash = np.zeros_like(a, bool)

		while True:
			y, x = np.where(np.logical_and(a > 9, np.invert(flash)))
			if len(y) == 0:
				break

			flash[y, x] = True
			for y1, x1 in zip(y, x):
				a[max(0, y1 - 1):y1 + 2, max(0, x1 - 1):x1 + 2] += 1

		flashes += np.count_nonzero(flash)
		a[flash] = 0

	return flashes


if __name__ == '__main__':
	import sys
	print(main(''.join(sys.stdin.readlines())))
