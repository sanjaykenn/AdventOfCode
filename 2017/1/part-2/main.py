import re


def main(inp):
	inp = inp.rstrip('\n')
	captcha = inp + inp[:len(inp) // 2]
	re_double = re.compile(f'(?=(\\d)\\d{{{len(inp) // 2 - 1}}}\\1)')

	return sum(map(int, re_double.findall(captcha)))


if __name__ == '__main__':
	import sys
	print(main(''.join(sys.stdin.readlines())))