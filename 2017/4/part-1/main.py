def main(inp):
	lines = inp.rstrip('\n').split('\n')
	return len(list(filter(lambda words: len(set(words)) == len(words), map(str.split, lines))))


if __name__ == '__main__':
	import sys
	print(main(''.join(sys.stdin.readlines())))
