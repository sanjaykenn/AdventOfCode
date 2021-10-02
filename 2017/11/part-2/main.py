def main(inp):
	x, y, z = 0, 0, 0
	best = 0
	for direction in inp.rstrip('\n').split(','):
		if direction == 'n':
			y += 1
			z -= 1
		elif direction == 's':
			y -= 1
			z += 1
		elif direction == 'ne':
			x += 1
			z -= 1
		elif direction == 'sw':
			x -= 1
			z += 1
		elif direction == 'nw':
			x -= 1
			y += 1
		elif direction == 'se':
			x += 1
			y -= 1

		best = max(best, max(map(abs, [x, y, z])))

	return best


if __name__ == '__main__':
	import sys
	print(main(''.join(sys.stdin.readlines())))
