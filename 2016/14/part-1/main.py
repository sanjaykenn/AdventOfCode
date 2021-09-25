import hashlib
import itertools
import re


def main(inp):
	salt = inp.rstrip('\n')
	re_tripple = re.compile('(.)\\1{2}')

	def is_key(index):
		c = re_tripple.search(hashlib.md5(f'{salt}{index}'.encode()).hexdigest())
		if c is None:
			return False

		c = c.group(1)

		for ind in range(index + 1, index + 1001):
			if c * 5 in hashlib.md5(f'{salt}{ind}'.encode()).hexdigest():
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
