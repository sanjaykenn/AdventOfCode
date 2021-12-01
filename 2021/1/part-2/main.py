import numpy as np


def main(inp):
	a = np.array(list(map(int, inp.splitlines())))
	return np.count_nonzero(a[:-3] < a[3:])


if __name__ == '__main__':
	import sys
	print(main(''.join(sys.stdin.readlines())))
