import re

import numpy as np


def main(inp):
	re_particle = re.compile(
		'^p=<-?\\d+,-?\\d+,-?\\d+>, v=<-?\\d+,-?\\d+,-?\\d+>, a=<(-?\\d+),(-?\\d+),(-?\\d+)>$'
	)
	accelerations = []
	for line in inp.rstrip('\n').split('\n'):
		accelerations.append(list(map(int, re_particle.match(line).groups())))

	return np.argmin(np.sum(np.abs(accelerations), 1))


if __name__ == '__main__':
	import sys
	print(main(''.join(sys.stdin.readlines())))
