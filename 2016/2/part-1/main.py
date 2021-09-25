def main(inp):
	x, y = 1, 1
	code = []

	for line in inp.rstrip('\n').split('\n'):
		for direction in line:
			if direction == 'U':
				y -= 1
			elif direction == 'R':
				x += 1
			elif direction == 'D':
				y += 1
			elif direction == 'L':
				x -= 1

			x = max(0, min(2, x))
			y = max(0, min(2, y))

		code.append(f'{y * 3 + x + 1}')

	return ''.join(code)


if __name__ == '__main__':
	import sys
	print(main(''.join(sys.stdin.readlines())))
