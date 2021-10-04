import re

import numpy as np


def main(inp):
	re_enhancement = re.compile('^([.#/]*) => ([.#/]*)$')

	pattern = np.array([
		[0, 1, 0],
		[0, 0, 1],
		[1, 1, 1]
	], dtype=bool)

	enhancements = {}
	for line in inp.rstrip('\n').split('\n'):
		a, b = re_enhancement.match(line).groups()
		a = np.array(list(map(list, a.split('/')))) == '#'
		b = np.array(list(map(list, b.split('/')))) == '#'
		for i in range(4):
			enhancements[tuple(map(tuple, a))] = b
			enhancements[tuple(map(tuple, np.flip(a, 0)))] = b
			a = np.rot90(a)

	def enhance(p):
		return enhancements[tuple(map(tuple, p))]

	for _ in range(5):
		s = 2 if pattern.shape[0] & 1 == 0 else 3
		pattern = np.array(list(map(
			enhance,
			pattern.reshape(pattern.shape[0] // s, s, -1, s).swapaxes(1, 2).reshape(-1, s, s)
		)))
		s1 = int(np.sqrt(np.size(pattern)))
		pattern = pattern.reshape(s1 // pattern.shape[1], -1, pattern.shape[1], pattern.shape[1]).swapaxes(1, 2).reshape(s1, s1)

	return pattern.sum()


if __name__ == '__main__':
	import sys
	print(main(''.join(sys.stdin.readlines())))
