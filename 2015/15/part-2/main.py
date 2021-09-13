import re

import numpy as np


def main(inp):
	r = re.compile('^.*: capacity (.*), durability (.*), flavor (.*), texture (.*), calories (.*)$')
	a = []
	calories = []

	for line in inp[:-1].split('\n'):
		*rst, c = r.match(line).groups()
		a.append(list(map(int, rst)))
		calories.append(int(c))

	a = np.array(a)
	calories = np.array(calories)

	def get_weights(weight_sum, size):
		if size == 1:
			yield weight_sum,
		else:
			for w1 in range(weight_sum + 1):
				for w2 in get_weights(weight_sum - w1, size - 1):
					yield (w1, ) + w2

	return max(map(
		lambda w: np.prod(np.maximum(np.sum(w[:, None] * a, 0), 0)),
		filter(
			lambda w: np.sum(w * calories) == 500,
			map(np.array, get_weights(100, len(a)))
		)
	))


if __name__ == '__main__':
	import sys
	print(main(''.join(sys.stdin.readlines())))
