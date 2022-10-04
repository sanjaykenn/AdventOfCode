import itertools
import re


def main(inp):
	r = re.compile('^([a-z]+) x=(-?\\d+)\\.\\.(-?\\d+),y=(-?\\d+)\\.\\.(-?\\d+),z=(-?\\d+)\\.\\.(-?\\d+)$')
	cubes_on = set()

	for line in inp.splitlines():
		state, *coords = r.match(line).groups()
		x1, x2, y1, y2, z1, z2 = map(int, coords)
		x1, y1, z1 = (max(a, -50) for a in [x1, y1, z1])
		x2, y2, z2 = (min(a, 50) + 1 for a in [x2, y2, z2])
		cubes = set(itertools.product(range(x1, x2), range(y1, y2), range(z1, z2)))

		if state == 'on':
			cubes_on |= cubes
		else:
			cubes_on -= cubes

	return len(cubes_on)


if __name__ == '__main__':
	import sys
	print(main(''.join(sys.stdin.readlines())))
