import itertools

import sympy


def main(inp):
	presents = int(inp.rstrip('\n'))

	def get_presents(n):
		if n == 1:
			return 10

		p, k = zip(*[(p, k) for p, k in sympy.ntheory.factorint(n).items()])
		result = 0

		for pot in itertools.product(*map(lambda x: range(x + 1), k)):
			x = 1
			for i in range(len(pot)):
				x *= p[i] ** pot[i]

			result += x

		return result * 10

	for house in itertools.count(1):
		if get_presents(house) > presents:
			return house


if __name__ == '__main__':
	import sys
	print(main(''.join(sys.stdin.readlines())))
