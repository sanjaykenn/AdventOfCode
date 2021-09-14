import itertools


def main(inp):
	sizes = list(map(int, inp[:-1].split('\n')))
	count = 0

	for size in range(1, len(sizes) + 1):
		count += len(list(filter(
			lambda a: sum(a) == 150,
			itertools.combinations(sizes, r=size)
		)))

	return count


if __name__ == '__main__':
	import sys
	print(main(''.join(sys.stdin.readlines())))
