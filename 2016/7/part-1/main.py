import re


def main(inp):
	re_brackets = re.compile('\\[(.*?)]')
	re_abba = re.compile('([a-z])([a-z])\\2\\1')
	count = 0

	for line in inp.strip('\n').split('\n'):
		for hypernet in re_brackets.findall(line):
			m = re_abba.search(hypernet)
			if m is None:
				continue

			if m.groups()[0] != m.groups()[1]:
				break
		else:
			m = re_abba.search(re_brackets.sub('.', line))
			if m is None:
				continue

			if m.groups()[0] != m.groups()[1]:
				count += 1

	return count


if __name__ == '__main__':
	import sys

	print(main(''.join(sys.stdin.readlines())))
