import numpy as np


def main(inp):
	inp = [tuple(map(int, line.split(': '))) for line in inp.rstrip('\n').split('\n')]
	depths = np.array(list(zip(*inp))[0])
	ranges = np.array(list(zip(*inp))[1])
	position = np.abs(depths % (2 * (ranges - 1)))
	hits, = np.where(position == 0)

	return sum(depths[hits] * ranges[hits])


if __name__ == '__main__':
	import sys
	print(main(''.join(sys.stdin.readlines())))
