def main(inp):
	count = 0

	for line in inp.rstrip('\n').split('\n'):
		x, y, z = sorted(map(int, line.strip().split()))
		if x + y > z:
			count += 1

	return count


if __name__ == '__main__':
	import sys
	print(main(''.join(sys.stdin.readlines())))
