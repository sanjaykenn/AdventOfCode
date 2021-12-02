def main(inp):
	horizontal, depth = 0, 0

	for line in inp.splitlines():
		direction, steps = line.split()
		steps = int(steps)

		if direction == 'forward':
			horizontal += steps
		elif direction == 'down':
			depth += steps
		elif direction == 'up':
			depth -= steps

	return horizontal * depth


if __name__ == '__main__':
	import sys
	print(main(''.join(sys.stdin.readlines())))
