import functools
import itertools
import math


operations = [
	sum,
	math.prod,
	min,
	max,
	None,
	lambda args: int(args[0] > args[1]),
	lambda args: int(args[0] < args[1]),
	lambda args: int(args[0] == args[1]),
]


def bitmap_to_int(iterator):
	return functools.reduce(lambda x, y: x << 1 | y, iterator)


def parse_packet(packet):
	packet = iter(packet)
	[next(packet) for _ in range(3)]
	type_id = bitmap_to_int(itertools.islice(packet, 3))

	if type_id == 4:
		value = 0
		while next(packet):
			value = value << 4 | bitmap_to_int(itertools.islice(packet, 4))

		return value << 4 | bitmap_to_int(itertools.islice(packet, 4))
	else:
		if next(packet):
			return operations[type_id]([parse_packet(packet) for _ in range(bitmap_to_int(itertools.islice(packet, 11)))])
		else:
			values = []
			sub_packets = itertools.islice(packet, bitmap_to_int(itertools.islice(packet, 15)))

			while True:
				try:
					values.append(parse_packet(sub_packets))
				except StopIteration:
					break

			return operations[type_id](values)


def main(inp):
	packet = list(map(int, bin(int(inp, 16))[2:]))
	packet = [0] * (-len(packet) & 3) + packet

	return parse_packet(packet)


if __name__ == '__main__':
	import sys
	print(main(''.join(sys.stdin.readlines())))
