import numpy as np


def main(inp):
	a = np.array(list(map(list, inp.splitlines())), dtype=int)

	g = np.sum((a.sum(0) > a.shape[0] // 2) * np.left_shift(1, np.arange(a.shape[1]))[::-1])
	e = np.sum((a.sum(0) < a.shape[0] // 2) * np.left_shift(1, np.arange(a.shape[1]))[::-1])

	return e*g


if __name__ == '__main__':
	import sys
	print(main(''.join(sys.stdin.readlines())))
