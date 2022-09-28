import itertools
import re


def hits_target(x1, x2, y1, y2, x_velocity, y_velocity):
	x = 0
	y = 0

	for xv, yv in itertools.zip_longest(range(x_velocity, 0, -1), itertools.count(y_velocity, -1), fillvalue=0):
		if x > x2 or y < y1 and yv <= 0:
			return False

		x += xv
		y += yv

		if x1 <= x <= x2 and y1 <= y <= y2:
			return True


def main(inp):
	x1, x2, y1, y2 = map(int, re.match('^target area: x=(-?\\d+)\\.\\.(-?\\d+), y=(-?\\d+)\\.\\.(-?\\d+)$', inp).groups())
	yv_max = max(abs(y1), abs(y2))

	return sum(
		hits_target(x1, x2, y1, y2, xv, yv) for xv, yv in itertools.product(range(x2 + 1), range(-yv_max, yv_max + 1))
	)


if __name__ == '__main__':
	import sys
	print(main(''.join(sys.stdin.readlines())))
