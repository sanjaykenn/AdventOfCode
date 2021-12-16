import functools
import itertools


def bitmap_to_int(iterator):
	return functools.reduce(lambda x, y: x << 1 | y, iterator)


def parse_packet(packet):
	packet = iter(packet)
	version = bitmap_to_int([next(packet) for _ in range(3)])
	type_id = bitmap_to_int(itertools.islice(packet, 3))

	if type_id == 4:
		while next(packet):
			list(itertools.islice(packet, 4))

		list(itertools.islice(packet, 4))
		return version
	else:
		if next(packet):
			return version + sum(parse_packet(packet) for _ in range(bitmap_to_int(itertools.islice(packet, 11))))
		else:
			version_sum = version
			sub_packets = itertools.islice(packet, bitmap_to_int(itertools.islice(packet, 15)))

			while True:
				try:
					version_sum += parse_packet(sub_packets)
				except StopIteration:
					break

			return version_sum


def main(inp):
	packet = list(map(int, bin(int(inp, 16))[2:]))
	packet = [0] * (-len(packet) & 3) + packet

	return parse_packet(packet)


if __name__ == '__main__':
	import sys
	print(main(''.join(sys.stdin.readlines())))
