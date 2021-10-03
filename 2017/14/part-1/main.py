import functools
import operator
from collections import deque


def main(inp):
	def knot_hash(value):
		lengths = list(map(ord, value)) + [17, 31, 73, 47, 23]

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

	inp = inp.rstrip('\n')
	return sum(map(
		lambda i: sum(map(lambda x: bin(int(x, 16)).count('1'), knot_hash(f'{inp}-{i}'))),
		range(128)
	))


if __name__ == '__main__':
	import sys
	print(main(''.join(sys.stdin.readlines())))
