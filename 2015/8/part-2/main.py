def main(inp):
	count = 0

	for line in inp[:-1].split('\n'):
		count += line.count('"') + line.count('\\') + 2

	return count


if __name__ == '__main__':
	import sys
	print(main(''.join(sys.stdin.readlines())))
