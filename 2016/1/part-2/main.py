def main(inp):
	x, y = 0, 0
	dx, dy = 0, -1
	visited = {(0, 0)}

	for step in inp.rstrip('\n').split(', '):
		turn, forward = step[0], int(step[1:])
		if turn == 'R':
			dx, dy = -dy, dx
		elif turn == 'L':
			dx, dy = dy, -dx

		for f in range(forward):
			x += dx
			y += dy

			if (x, y) in visited:
				return abs(x) + abs(y)

			visited.add((x, y))


if __name__ == '__main__':
	import sys
	print(main(''.join(sys.stdin.readlines())))
