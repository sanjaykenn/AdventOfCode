def main(inp):
	return max(sum(map(int, inventory.splitlines())) for inventory in inp.split('\n\n'))


if __name__ == '__main__':
	import sys
	print(main(''.join(sys.stdin.readlines())))
