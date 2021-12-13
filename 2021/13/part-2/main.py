import re

import numpy as np
from matplotlib import pyplot as plt


def main(inp):
	r = re.compile('^fold along ([xy])=(\\d+)$')
	points, folds = inp.rstrip('\n').split('\n\n')
	x, y = zip(*[map(int, line.split(',')) for line in points.splitlines()])

	paper = np.zeros((max(y) + 1, max(x) + 1), dtype=bool)
	paper[y, x] = True

	for line in folds.splitlines():
		axis, coord = r.match(line).groups()
		coord = int(coord)
		if axis == 'x':
			a = paper[:, :coord:-1]
			paper = paper[:, :coord]
			paper[:, -a.shape[1]:] = np.logical_or(paper[:, -a.shape[1]:], a)
		elif axis == 'y':
			a = paper[:coord:-1]
			paper = paper[:coord]
			paper[-a.shape[0]:] = np.logical_or(paper[-a.shape[0]:], a)

	plt.gca().axes.get_xaxis().set_visible(False)
	plt.gca().axes.get_yaxis().set_visible(False)
	plt.gca().spines['top'].set_visible(False)
	plt.gca().spines['right'].set_visible(False)
	plt.gca().spines['bottom'].set_visible(False)
	plt.gca().spines['left'].set_visible(False)

	plt.imshow(paper, cmap='Greys')

	plt.savefig('output.png')
	plt.show()


if __name__ == '__main__':
	import sys
	print(main(''.join(sys.stdin.readlines())))
