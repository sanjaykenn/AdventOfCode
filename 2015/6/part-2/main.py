import re

import numpy as np


def main(inp):
	re_command = re.compile('^(.*) (\\d+),(\\d+) through (\\d+),(\\d+)$')
	lights = np.zeros((1000, 1000), dtype=int)

	for line in inp[:-1].split('\n'):
		command, x1, y1, x2, y2 = re_command.match(line).groups()
		x1, y1, x2, y2 = map(int, [x1, y1, x2, y2])
		x2 += 1
		y2 += 1

		if command == 'turn on':
			lights[x1:x2, y1:y2] += 1
		elif command == 'turn off':
			lights[x1:x2, y1:y2] -= 1
			lights[lights < 0] = 0
		else:
			lights[x1:x2, y1:y2] += 2

	return np.sum(lights)


if __name__ == '__main__':
	import sys

	print(main(''.join(sys.stdin.readlines())))
