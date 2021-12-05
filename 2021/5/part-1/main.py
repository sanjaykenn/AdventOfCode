import re
from collections import defaultdict


def main(inp):
	r = re.compile('^(\\d+),(\\d+) -> (\\d+),(\\d+)$')
	coords = defaultdict(int)

	for line in inp.splitlines():
		x1, y1, x2, y2 = map(int, r.match(line).groups())
		x1, x2 = sorted([x1, x2])
		y1, y2 = sorted([y1, y2])

		if x1 == x2:
			for y in range(y1, y2 + 1):
				coords[x1, y] += 1
		elif y1 == y2:
			for x in range(x1, x2 + 1):
				coords[x, y1] += 1

	return len([0 for v in coords.values() if v >= 2])


if __name__ == '__main__':
	import sys
	print(main(''.join(sys.stdin.readlines())))
