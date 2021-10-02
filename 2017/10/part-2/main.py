import functools
import operator
from collections import deque


def main(inp):
	lengths = list(map(ord, inp.rstrip('\n'))) + [17, 31, 73, 47, 23]

	numbers = deque(range(256))
	position = 0
	skip_size = 0

	for _ in range(64):
		for length in lengths:
			numbers.rotate(-position)
			numbers = list(numbers)
			numbers[:length] = list(reversed(numbers[:length]))
			numbers = deque(numbers)
			numbers.rotate(position)

			position = (position + length + skip_size) % len(numbers)
			skip_size += 1

	numbers = list(numbers)

	dense = []
	for block in range(0, 256, 16):
		dense.append(functools.reduce(operator.xor, numbers[block:block + 16]))

	return ''.join(map('{:02x}'.format, dense))


if __name__ == '__main__':
	import sys
	print(main(''.join(sys.stdin.readlines())))
