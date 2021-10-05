from collections import Counter


def main(inp):
	words = list(map(Counter, inp.rstrip('\n').split('\n')))
	a = len(list(filter(lambda word: 2 in word.values(), words)))
	b = len(list(filter(lambda word: 3 in word.values(), words)))

	return a*b


if __name__ == '__main__':
	import sys
	print(main(''.join(sys.stdin.readlines())))
