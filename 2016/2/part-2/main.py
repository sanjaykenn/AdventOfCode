def main(inp):
	x, y = 0, 2
	code = []
	field = ['  1  ', ' 234 ', '56789', ' ABC ', '  D  ']

	for line in inp.rstrip('\n').split('\n'):
		for direction in line:
			px, py = x, y

			if direction == 'U':
				y -= 1
			elif direction == 'R':
				x += 1
			elif direction == 'D':
				y += 1
			elif direction == 'L':
				x -= 1

			if not (0 <= x < 5) or not (0 <= y < 5) or field[y][x] == ' ':
				x, y = px, py

		code.append(field[y][x])

	return ''.join(code)


if __name__ == '__main__':
	import sys
	print(main(''.join(sys.stdin.readlines())))
