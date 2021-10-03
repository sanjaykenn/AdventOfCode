def main(inp):
	field = inp.rstrip('\n').split('\n')
	y = 0
	x = field[0].index('|')
	dx = 0
	dy = 1
	result = ''

	while True:
		if field[y][x] == ' ':
			return result
		elif field[y][x] == '+':
			for ndx, ndy in {(0, -1), (-1, 0), (1, 0), (0, 1)} - {(-dx, -dy)}:
				x1, y1 = x + ndx, y + ndy
				if 0 <= y1 < len(field) and 0 <= x1 < len(field[y1]) and field[y1][x1] != ' ':
					dx, dy = ndx, ndy
					break
		elif field[y][x].isalpha():
			result += field[y][x]

		x += dx
		y += dy


if __name__ == '__main__':
	import sys
	print(main(''.join(sys.stdin.readlines())))
