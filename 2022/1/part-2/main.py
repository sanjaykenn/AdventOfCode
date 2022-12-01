def main(inp):
	a = sorted(sum(map(int, inventory.splitlines())) for inventory in inp.split('\n\n'))
	return sum(a[-3:])


if __name__ == '__main__':
	import sys
	print(main(''.join(sys.stdin.readlines())))
