import re


def main(inp):
	re_brackets = re.compile('\\[(.*?)]')
	re_aba = re.compile('(?=([a-z])([a-z])\\1)')
	count = 0

	for line in inp.strip('\n').split('\n'):
		babs = set()
		for hypernet in re_brackets.findall(line):
			for b, a in re_aba.findall(hypernet):
				if a != b:
					babs.add((a, b))

		for a, b in re_aba.findall(re_brackets.sub('.', line)):
			if (a, b) in babs:
				count += 1
				break

	return count


if __name__ == '__main__':
	import sys
	print(main(''.join(sys.stdin.readlines())))
