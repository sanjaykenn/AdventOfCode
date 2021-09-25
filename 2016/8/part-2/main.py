import re

import numpy as np


def main(inp):
	lights = np.zeros((6, 50), dtype=bool)

	re_rect = re.compile('^rect (\\d+)x(\\d+)$')
	re_row = re.compile('^rotate row y=(\\d+) by (\\d+)$')
	re_col = re.compile('^rotate column x=(\\d+) by (\\d+)$')

	for line in inp.strip('\n').split('\n'):
		m = re_rect.match(line)
		if m:
			a, b = map(int, m.groups())
			lights[:b, :a] = True
			continue

		m = re_row.match(line)
		if m:
			a, b = map(int, m.groups())
			lights[a] = np.roll(lights[a], b)
			continue

		m = re_col.match(line)
		if m:
			a, b = map(int, m.groups())
			lights[:, a] = np.roll(lights[:, a], b)
			continue

	print('\n'.join(map(
		lambda row: ''.join(map(lambda cell: ['.', '#'][cell], row)),
		lights
	)))


if __name__ == '__main__':
	import sys
	print(main(''.join(sys.stdin.readlines())))
