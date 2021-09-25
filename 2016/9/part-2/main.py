import re


def main(inp):
	re_parenthese = re.compile('\\((\\d+)x(\\d+)\\)')

	def get_decompressed_length(compressed):
		i = 0
		result = 0
		while i < len(compressed):
			m = re_parenthese.search(compressed, pos=i)

			if m is None:
				return result + len(compressed) - i

			length, repeat = map(int, m.groups())
			l1 = get_decompressed_length(compressed[m.end():m.end() + length])
			result += m.start() - i + l1 * repeat
			i = m.end() + length

		return result

	return get_decompressed_length(inp.rstrip('\n'))


if __name__ == '__main__':
	import sys
	print(main(''.join(sys.stdin.readlines())))
