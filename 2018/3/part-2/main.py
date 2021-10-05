import re

import numpy as np


def main(inp):
	re_row = re.compile('^#(\\d+) @ (\\d+),(\\d+): (\\d+)x(\\d+)$')
	field = np.zeros((1000, 1000), dtype=int)
	free = set()

	for line in inp.rstrip('\n').split('\n'):
		i, x, y, a, b = map(int, re_row.match(line).groups())
		f = field[y:y+b, x:x+a]
		if np.all(f == 0):
			free.add(i)
		else:
			free -= set(f.reshape(-1))

		f[:, :] = i

	return min(free)


if __name__ == '__main__':
	import sys
	print(main(''.join(sys.stdin.readlines())))
