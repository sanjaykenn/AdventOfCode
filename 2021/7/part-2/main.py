import numpy as np


def main(inp):
	a = np.array(list(map(int, inp.split(','))))
	best = np.inf

	for i in range(max(a)):
		n = np.abs(i - a)
		best = min(best, np.sum(n * (n + 1) // 2))

	return best


if __name__ == '__main__':
	import sys
	print(main(''.join(sys.stdin.readlines())))
