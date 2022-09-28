import functools
import json
import math


def increase_leftmost(a, v):
	if isinstance(a[0], list):
		increase_leftmost(a[0], v)
	else:
		a[0] += v


def increase_rightmost(a, v):
	if isinstance(a[1], list):
		increase_rightmost(a[1], v)
	else:
		a[1] += v


def apply_explosions(a, n=0):
	left, right = 0, 0

	if isinstance(a[0], list):
		if n < 3:
			left, y = apply_explosions(a[0], n + 1)
		else:
			left, y = a[0]
			a[0] = 0

		if isinstance(a[1], list):
			increase_leftmost(a[1], y)
		else:
			a[1] += y

	if isinstance(a[1], list):
		if n < 3:
			x, right = apply_explosions(a[1], n + 1)
		else:
			x, right = a[1]
			a[1] = 0

		if isinstance(a[0], list):
			increase_rightmost(a[0], x)
		else:
			a[0] += x

	return left, right


def apply_split(a):
	for i in range(len(a)):
		if isinstance(a[i], list):
			if apply_split(a[i]):
				return True
		elif a[i] >= 10:
			a[i] = [math.floor(a[i] / 2), math.ceil(a[i] / 2)]
			return True

	return False


def add(a, b):
	c = [a, b]
	apply_explosions(c)
	while apply_split(c):
		apply_explosions(c)

	return c


def magnitude(a):
	if isinstance(a, list):
		return 3*magnitude(a[0]) + 2*magnitude(a[1])

	return a


def main(inp):
	return magnitude(functools.reduce(add, map(json.loads, inp.splitlines())))


if __name__ == '__main__':
	import sys
	print(main(''.join(sys.stdin.readlines())))
