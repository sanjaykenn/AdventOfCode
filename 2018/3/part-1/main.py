import re

import numpy as np


def main(inp):
	re_row = re.compile('^#\\d+ @ (\\d+),(\\d+): (\\d+)x(\\d+)$')
	field = np.zeros((1000, 1000), dtype=int)

	for line in inp.rstrip('\n').split('\n'):
		x, y, a, b = map(int, re_row.match(line).groups())
		field[y:y+b, x:x+a] += 1

	return np.sum(field >= 2)


if __name__ == '__main__':
	import sys
	print(main(''.join(sys.stdin.readlines())))
