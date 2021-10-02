import re


def main(inp):
	re_double = re.compile('(?=(\\d)\\1)')
	inp = inp.rstrip('\n')
	captcha = inp + inp[0]
	return sum(map(int, re_double.findall(captcha)))


if __name__ == '__main__':
	import sys
	print(main(''.join(sys.stdin.readlines())))
