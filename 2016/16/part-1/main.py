import numpy as np


def main(inp):
	a = np.array(list(inp.rstrip('\n'))) == '1'
	length = 272

	while len(a) < length:
		a = np.concatenate((a, [0], np.logical_not(a)[::-1]))

	a = a[:length]

	while len(a) & 1 == 0:
		a = np.logical_not(np.bitwise_xor(a[::2], a[1::2]))

	return ''.join(map(str, np.array(a, dtype=int)))


if __name__ == '__main__':
	import sys
	print(main(''.join(sys.stdin.readlines())))
