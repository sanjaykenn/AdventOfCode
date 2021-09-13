import re


def main(inp):
	r = re.compile('(\\d)(\\1*)')
	x = inp.rstrip('\n')

	for i in range(40):
		x = ''.join(map(lambda a: f'{len(a[1]) + 1}{a[0]}', r.findall(x)))

	return len(x)


if __name__ == '__main__':
	import sys
	print(main(''.join(sys.stdin.readlines())))
