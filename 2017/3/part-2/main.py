import itertools
import math


def main(inp):
	n = int(inp)

	values = {(0, 0): 1}
	neighbors = {(x, y) for x in range(-1, 2) for y in range(-1, 2)} - {(0, 0)}

	x, y = 0, 0
	for i in itertools.count(2):
		x += int(math.sin(math.floor(math.sqrt(4*i - 7)) * math.pi / 2))
		y += int(math.cos(math.floor(math.sqrt(4*i - 7)) * math.pi / 2))
		value = 0
		for dx, dy in neighbors:
			value += values.get((x + dx, y + dy), 0)

		values[x, y] = value

		if value > n:
			return value


if __name__ == '__main__':
	import sys
	print(main(''.join(sys.stdin.readlines())))
