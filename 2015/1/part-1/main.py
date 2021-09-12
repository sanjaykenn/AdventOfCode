def main(inp):
	return inp.count('(') - inp.count(')')


if __name__ == '__main__':
	import sys
	print(main(''.join(sys.stdin.readlines())))
