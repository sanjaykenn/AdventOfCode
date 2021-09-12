import re


def main(inp):
	r = re.compile('(\\d+)x(\\d+)x(\\d+)')
	a = 0

	for line in inp[:-1].split('\n'):
		l, w, h = map(int, r.match(line).groups())
		a += 2*(l*w + w*h + h*l) + min(l*w, w*h, h*l)

	return a


if __name__ == '__main__':
	import sys
	print(main(''.join(sys.stdin.readlines())))
