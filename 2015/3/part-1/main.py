def main(inp):
	x = 0
	y = 0
	visited = {(0, 0)}
	for direction in inp[:-1]:
		if direction == '>':
			x += 1
		elif direction == '<':
			x -= 1
		elif direction == '^':
			y -= 1
		elif direction == 'v':
			y += 1

		visited.add((x, y))

	return len(visited)


if __name__ == '__main__':
	import sys
	print(main(''.join(sys.stdin.readlines())))
