def main(inp):
	x, y = 0, 0
	dx, dy = 0, -1

	for step in inp.rstrip('\n').split(', '):
		turn, forward = step[0], int(step[1:])
		if turn == 'R':
			dx, dy = -dy, dx
		elif turn == 'L':
			dx, dy = dy, -dx

		x += forward * dx
		y += forward * dy

	return abs(x) + abs(y)


if __name__ == '__main__':
	import sys
	print(main(''.join(sys.stdin.readlines())))
