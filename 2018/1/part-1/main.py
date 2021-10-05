def main(inp):
	return sum(map(int, inp.rstrip('\n').split('\n')))


if __name__ == '__main__':
	import sys
	print(main(''.join(sys.stdin.readlines())))
