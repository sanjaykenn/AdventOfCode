import itertools
import re

import numpy as np


def main(inp):
	re_disc = re.compile('^Disc #\\d+ has (\\d+) positions; at time=0, it is at position (\\d+)\\.$')
	modul = []
	position = []

	for line in inp.rstrip('\n').split('\n'):
		m, p = map(int, re_disc.match(line).groups())
		modul.append(m)
		position.append(p)

	modul = np.array(modul)
	position = np.array(position)
	indexes = np.arange(1, len(modul) + 1)

	for t in itertools.count():
		if all((position + indexes + t) % modul == 0):
			return t


if __name__ == '__main__':
	import sys
	print(main(''.join(sys.stdin.readlines())))
