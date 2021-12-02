def main(inp):
	horizontal, depth, aim = 0, 0, 0

	for line in inp.splitlines():
		direction, steps = line.split()
		steps = int(steps)

		if direction == 'forward':
			horizontal += steps
			depth += aim * steps
		elif direction == 'down':
			aim += steps
		elif direction == 'up':
			aim -= steps

	return horizontal * depth


if __name__ == '__main__':
	import sys
	print(main(''.join(sys.stdin.readlines())))
