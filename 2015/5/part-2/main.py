import re


def main(inp):
	re_double_twice = re.compile('(.)(.).*\\1\\2')
	re_double_between = re.compile('(.).\\1')
	count = 0

	for line in inp[:-1].split('\n'):
		if re_double_twice.search(line) and re_double_between.search(line):
			count += 1

	return count


if __name__ == '__main__':
	import sys

	print(main(''.join(sys.stdin.readlines())))
