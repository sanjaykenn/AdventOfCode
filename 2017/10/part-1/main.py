from collections import deque


def main(inp):
	lengths = map(int, inp.rstrip('\n').split(','))

	numbers = deque(range(256))
	position = 0

	for skip_size, length in enumerate(lengths):
		numbers.rotate(-position)
		numbers = list(numbers)
		numbers[:length] = list(reversed(numbers[:length]))
		numbers = deque(numbers)
		numbers.rotate(position)

		position = (position + length + skip_size) % len(numbers)

	return numbers[0] * numbers[1]


if __name__ == '__main__':
	import sys
	print(main(''.join(sys.stdin.readlines())))
