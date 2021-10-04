def main(inp):
	field = inp.rstrip('\n').split('\n')
	infected = set()
	result = 0

	for y in range(len(field)):
		for x in range(len(field[y])):
			if field[y][x] == '#':
				infected.add((x, y))

	y = len(field) // 2
	x = len(field[y]) // 2
	dx, dy = 0, -1
	for _ in range(10000):
		if (x, y) in infected:
			dx, dy = -dy, dx
			infected.remove((x, y))
		else:
			dx, dy = dy, -dx
			infected.add((x, y))
			result += 1

		x += dx
		y += dy

	return result


if __name__ == '__main__':
	import sys
	print(main(''.join(sys.stdin.readlines())))
