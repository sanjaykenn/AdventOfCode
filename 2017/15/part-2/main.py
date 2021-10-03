import re


def main(inp):
	re_generators = re.compile('^Generator A starts with (\\d+)\nGenerator B starts with (\\d+)$')
	a, b = map(int, re_generators.match(inp.rstrip('\n')).groups())
	factor_a, factor_b = 16807, 48271
	mod = 2147483647
	bits = 65535
	result = 0

	for i in range(5_000_000):
		while True:
			a = a * factor_a % mod
			if a & 3 == 0: break

		while True:
			b = b * factor_b % mod
			if b & 7 == 0: break

		if a & bits == b & bits:
			result += 1

	return result


if __name__ == '__main__':
	import sys
	print(main(''.join(sys.stdin.readlines())))
