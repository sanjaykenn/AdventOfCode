import itertools

import numpy as np


def main(inp):
	words = map(lambda word: np.array(list(word)), inp.rstrip('\n').split('\n'))
	result = ''
	for word1, word2 in itertools.combinations(words, r=2):
		s = ''.join(word1[word1 == word2])
		result = max(s, result, key=len)

	return result


if __name__ == '__main__':
	import sys
	print(main(''.join(sys.stdin.readlines())))
