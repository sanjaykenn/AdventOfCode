def main(inp):
	a = list(map(int, inp.splitlines()))
	result = 0

	for i, j in zip(a, a[1:]):
		if j > i:
			result += 1

	return result


if __name__ == '__main__':
	import sys
	print(main(''.join(sys.stdin.readlines())))
