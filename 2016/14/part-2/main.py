import hashlib
import itertools
import re


def main(inp):
	salt = inp.rstrip('\n')
	re_tripple = re.compile('(.)\\1{2}')

	cache = {}

	def md5_cycled(a, cycles=2017):
		if a in cache:
			return cache[a]

		h = a
		for _ in range(cycles):
			h = hashlib.md5(h.encode()).hexdigest()

		cache[a] = h
		return h

	def is_key(index):
		c = re_tripple.search(md5_cycled(f'{salt}{index}'))
		if c is None:
			return False

		c = c.group(1)

		for ind in range(index + 1, index + 1001):
			if c * 5 in md5_cycled(f'{salt}{ind}'):
				return True

		return False

	count = 0
	for i in itertools.count():
		if is_key(i):
			count += 1
			if count == 64:
				return i


if __name__ == '__main__':
	import sys
	print(main(''.join(sys.stdin.readlines())))
