import numpy as np


def main(inp):
	a = np.cumsum([0] + list(map(int, inp.splitlines())))
	return np.count_nonzero(a[3:-1] - a[:-4] < a[4:] - a[1:-3])


if __name__ == '__main__':
	import sys
	print(main(''.join(sys.stdin.readlines())))
