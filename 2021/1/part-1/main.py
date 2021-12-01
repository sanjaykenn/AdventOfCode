import numpy as np


def main(inp):
	a = np.array(list(map(int, inp.splitlines())))
	return np.count_nonzero(a[:-1] < a[1:])


if __name__ == '__main__':
	import sys
	print(main(''.join(sys.stdin.readlines())))
