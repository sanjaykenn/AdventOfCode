import math


def main(inp):
	x, y = 0, 0
	for i in range(2, int(inp) + 1):
		x += int(math.sin(math.floor(math.sqrt(4*i - 7)) * math.pi / 2))
		y += int(math.cos(math.floor(math.sqrt(4*i - 7)) * math.pi / 2))

	return abs(int(x)) + abs(int(y))


if __name__ == '__main__':
	import sys
	print(main(''.join(sys.stdin.readlines())))
