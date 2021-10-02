def main(inp):
	return sum(map(
		lambda row: max(row) - min(row),
		map(
			lambda line: list(map(int, line.split())),
			inp.rstrip('\n').split('\n')
		)
	))


if __name__ == '__main__':
	import sys
	print(main(''.join(sys.stdin.readlines())))
