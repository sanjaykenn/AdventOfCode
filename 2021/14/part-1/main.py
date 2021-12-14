import math
from collections import defaultdict, Counter


def main(inp):
	n = 10
	word, rules_ = inp.split('\n\n')
	rules_ = [line.split(' -> ') for line in rules_.splitlines()]
	rules = {tuple(a): b for a, b in rules_}
	pairs = Counter(zip(word, word[1:]))

	for _ in range(n):
		new_pairs = defaultdict(int)
		for (a, b), count in pairs.items():
			new_char = rules[a, b]
			new_pairs[a, new_char] += count
			new_pairs[new_char, b] += count

		pairs = new_pairs

	letter_count = defaultdict(int)
	for (c1, c2), count in pairs.items():
		letter_count[c1] += count
		letter_count[c2] += count

	return math.ceil(max(letter_count.values()) / 2) - math.ceil(min(letter_count.values()) / 2)


if __name__ == '__main__':
	import sys
	print(main(''.join(sys.stdin.readlines())))
