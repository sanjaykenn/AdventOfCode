def main(inp):
	field = inp.rstrip('\n').split('\n')
	infected = {}
	result = 0

	for y in range(len(field)):
		for x in range(len(field[y])):
			if field[y][x] == '#':
				infected[x, y] = 2

	y = len(field) // 2
	x = len(field[y]) // 2
	dx, dy = 0, -1
	for _ in range(10000000):
		if (x, y) not in infected:
			dx, dy = dy, -dx
			infected[x, y] = 1
		elif infected[x, y] == 1:
			infected[x, y] = 2
			result += 1
		elif infected[x, y] == 2:
			dx, dy = -dy, dx
			infected[x, y] = 3
		elif infected[x, y] == 3:
			dx, dy = -dx, -dy
			del infected[x, y]

		x += dx
		y += dy

	return result


if __name__ == '__main__':
	import sys
	print(main(''.join(sys.stdin.readlines())))
