import itertools
import math


def main(inp):
	weights = set(map(int, inp[:-1].split('\n')))
	fourth_weight = sum(weights) // 4

	def has_combination(w, n=1):
		for s in range(len(w) + 1):
			for group2 in itertools.combinations(w, s):
				if sum(group2) == fourth_weight:
					if n == 0:
						return True
					elif has_combination(w - set(group2), n - 1):
						return True

		return False

	for size in range(len(weights) + 1):
		qe = math.inf
		for group1 in itertools.combinations(weights, size):
			if sum(group1) != fourth_weight:
				continue

			if has_combination(weights - set(group1)):
				qe = min(qe, math.prod(group1))

		if qe < math.inf:
			return qe


if __name__ == '__main__':
	import sys
	print(main(''.join(sys.stdin.readlines())))
