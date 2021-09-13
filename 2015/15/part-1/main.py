import re

import numpy as np


def main(inp):
	r = re.compile('^.*: capacity (.*), durability (.*), flavor (.*), texture (.*), calories .*$')
	a = []

	for line in inp[:-1].split('\n'):
		a.append(list(map(int, r.match(line).groups())))

	a = np.array(a)

	def get_weights(weight_sum, size):
		if size == 1:
			yield weight_sum,
		else:
			for w1 in range(weight_sum + 1):
				for w2 in get_weights(weight_sum - w1, size - 1):
					yield (w1, ) + w2

	return max(map(
		lambda w: np.prod(np.maximum(np.sum(np.array(w)[:, None] * a, 0), 0)),
		get_weights(100, len(a))
	))


if __name__ == '__main__':
	import sys
	print(main(''.join(sys.stdin.readlines())))
