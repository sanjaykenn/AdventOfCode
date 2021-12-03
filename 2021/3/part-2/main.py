import numpy as np


def main(inp):
	a = np.array(list(map(list, inp.splitlines())), dtype=int)
	g = a.copy()
	e = a.copy()

	for i in range(g.shape[1]):
		count_ones = g[:, i].sum() >= g.shape[0] / 2
		if count_ones:
			g = g[g[:, i] == 1]
		else:
			g = g[g[:, i] == 0]

		if g.shape[0] == 1:
			break

	for i in range(e.shape[1]):
		count_ones = e[:, i].sum() < e.shape[0] / 2
		if count_ones:
			e = e[e[:, i] == 1]
		else:
			e = e[e[:, i] == 0]

		if e.shape[0] == 1:
			break

	g1 = np.sum(g[0] * np.left_shift(1, np.arange(g.shape[1]))[::-1])
	e1 = np.sum(e[0] * np.left_shift(1, np.arange(g.shape[1]))[::-1])

	return g1 * e1


if __name__ == '__main__':
	import sys
	print(main(''.join(sys.stdin.readlines())))
