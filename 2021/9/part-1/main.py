def get_neighbors(x, y, a):
	for x1, y1 in [(x, y - 1), (x - 1, y), (x + 1, y), (x, y + 1)]:
		if 0 <= y1 < len(a) and 0 <= x1 < len(a[y]):
			yield x1, y1


def main(inp):
	a = [list(map(int, line)) for line in inp.splitlines()]
	result = 0

	for y in range(len(a)):
		for x in range(len(a[y])):
			for x1, y1 in get_neighbors(x, y, a):
				if a[y1][x1] <= a[y][x]:
					break
			else:
				result += a[y][x] + 1

	return result


if __name__ == '__main__':
	import sys
	print(main(''.join(sys.stdin.readlines())))
