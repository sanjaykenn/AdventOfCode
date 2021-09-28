import re


def main(inp):
	re_range = re.compile('^(\\d+)-(\\d+)$')
	ranges = set()

	for line in inp.rstrip('\n').split('\n'):
		start1, end1 = map(int, re_range.match(line).groups())
		while True:
			for start2, end2 in ranges:
				if end1 >= start2 - 1 and end2 >= start1 - 1:
					start1 = min(start1, start2)
					end1 = max(end1, end2)
					ranges.remove((start2, end2))
					break
			else:
				ranges.add((start1, end1))
				break

	return 4294967296 - sum(map(lambda r: r[1] - r[0] + 1, ranges))


if __name__ == '__main__':
	import sys
	print(main(''.join(sys.stdin.readlines())))
