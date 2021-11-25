import re
from collections import deque

import numpy as np


def main(inp):
	players, marbles = map(int, re.match('(\\d+) players; last marble is worth (\\d+) points', inp.rstrip('\n')).groups())
	players = np.zeros(players, int)
	circle = deque([0])

	for i in range(1, marbles * 100 + 1):
		if i % 23 == 0:
			players[i % len(players)] += i
			circle.rotate(7)
			players[i % len(players)] += circle.pop()
			circle.rotate(-1)
		else:
			circle.rotate(-1)
			circle.append(i)

	return max(players)


if __name__ == '__main__':
	import sys
	print(main(''.join(sys.stdin.readlines())))
