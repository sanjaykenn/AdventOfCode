import itertools

import numpy as np


def main(inp):
	inp = [tuple(map(int, line.split(': '))) for line in inp.rstrip('\n').split('\n')]
	depths = np.array(list(zip(*inp))[0])
	ranges = np.array(list(zip(*inp))[1])
	mod = 2 * (ranges - 1)

	for delay in itertools.count():
		try:
			next(filter(
				lambda b: (b[0] + delay) % b[1] == 0,
				zip(depths, mod)
			))
		except StopIteration:
			return delay


if __name__ == '__main__':
	import sys
	print(main(''.join(sys.stdin.readlines())))
