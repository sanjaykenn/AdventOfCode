import numpy as np


def main(inp):
	a = np.array(sorted(map(int, inp.split(','))))
	left = np.arange(1, len(a))
	fuel_change = (a[1:] - a[:-1]) * (left - left[::-1])
	return a.sum() + np.insert(fuel_change, 0, 0).cumsum().min()


if __name__ == '__main__':
	import sys
	print(main(''.join(sys.stdin.readlines())))
