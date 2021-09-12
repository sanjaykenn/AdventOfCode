import re


def main(inp):
	r = re.compile('(\\d+)x(\\d+)x(\\d+)')
	ribbon = 0

	for line in inp[:-1].split('\n'):
		l, w, h = map(int, r.match(line).groups())
		ribbon += 2*(l + w + h - max(l, w, h)) + l*w*h

	return ribbon


if __name__ == '__main__':
	import sys
	print(main(''.join(sys.stdin.readlines())))
