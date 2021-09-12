import hashlib
import itertools


def main(inp):
	key = inp.rstrip('\n')

	for i in itertools.count(1):
		if hashlib.md5(f'{key}{i}'.encode()).hexdigest().startswith('00000'):
			return i


if __name__ == '__main__':
	import sys

	print(main(''.join(sys.stdin.readlines())))
