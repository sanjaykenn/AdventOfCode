def main(inp):
	a = list(map(int, inp.splitlines()))
	result = 0

	for i, j, k, l in zip(a, a[1:], a[2:], a[3:]):
		if i + j + k < j + k + l:
			result += 1

	return result


if __name__ == '__main__':
	import sys
	print(main(''.join(sys.stdin.readlines())))
