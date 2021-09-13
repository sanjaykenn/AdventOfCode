import re


def main(inp):
	count = 0

	regs = [
		re.compile(r'\\\\'),
		re.compile(r'\\"'),
		re.compile(r'\\x..')
	]

	for line in inp[:-1].split('\n'):
		count += len(line)
		line = line[1:-1]

		for reg in regs:
			line = reg.sub('.', line)

		count -= len(line)

	return count


if __name__ == '__main__':
	import sys
	print(main(''.join(sys.stdin.readlines())))
