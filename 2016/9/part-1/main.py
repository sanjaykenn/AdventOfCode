import re


def main(inp):
	re_parenthese = re.compile('\\((\\d+)x(\\d+)\\)')
	compressed = inp.rstrip('\n')
	decompressed = ''
	i = 0
	while i < len(compressed):
		m = re_parenthese.search(compressed, pos=i)

		if m is None:
			return len(decompressed + compressed[i:])

		length, repeat = map(int, m.groups())
		decompressed += compressed[i:m.start()] + compressed[m.end():m.end() + length] * repeat
		i = m.end() + length

	return len(decompressed)


if __name__ == '__main__':
	import sys
	print(main(''.join(sys.stdin.readlines())))
