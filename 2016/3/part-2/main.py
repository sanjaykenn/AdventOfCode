import itertools


def main(inp):
	count = 0
	data = list(itertools.chain(*zip(*map(
		lambda line: list(map(int, line.strip().split())),
		inp.rstrip('\n').split('\n')
	))))

	for x, y, z in zip(data[::3], data[1::3], data[2::3]):
		x, y, z = sorted((x, y, z))
		if x + y > z:
			count += 1

	return count


if __name__ == '__main__':
	import sys

	print(main(''.join(sys.stdin.readlines())))
