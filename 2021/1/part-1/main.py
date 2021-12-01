import numpy as np


def main(inp):
	a = np.diff(list(map(int, inp.splitlines())))
	return np.count_nonzero(a > 0)


if __name__ == '__main__':
	import sys
	print(main(''.join(sys.stdin.readlines())))
