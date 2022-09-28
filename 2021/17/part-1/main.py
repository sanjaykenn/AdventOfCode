import re


def main(inp):
	y1 = int(re.match('^target area: x=-?\\d+\\.\\.-?\\d+, y=(-?\\d+)\\.\\.-?\\d+$', inp).group(1))
	return y1 * (y1 + 1) // 2


if __name__ == '__main__':
	import sys
	print(main(''.join(sys.stdin.readlines())))
