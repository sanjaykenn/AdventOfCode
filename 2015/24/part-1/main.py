import itertools
import math


def main(inp):
	weights = set(map(int, inp[:-1].split('\n')))
	third_weight = sum(weights) // 3

	def has_combination(w):
		for s in range(len(w) + 1):
			for group2 in itertools.combinations(w, s):
				if sum(group2) == third_weight:
					return True

		return False

	for size in range(len(weights) + 1):
		qe = math.inf
		for group1 in itertools.combinations(weights, size):
			if sum(group1) != third_weight:
				continue

			if has_combination(weights - set(group1)):
				qe = min(qe, math.prod(group1))

		if qe < math.inf:
			return qe


if __name__ == '__main__':
	import sys
	print(main(''.join(sys.stdin.readlines())))
