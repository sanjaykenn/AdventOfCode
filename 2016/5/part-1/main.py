import hashlib
import itertools


def main(inp):
	prefix = inp.rstrip('\n')
	password = ''

	for i in itertools.count():
		h = hashlib.md5(f'{prefix}{i}'.encode()).hexdigest()
		if h.startswith('00000'):
			password += h[5]
			if len(password) >= 8:
				return password


if __name__ == '__main__':
	import sys
	print(main(''.join(sys.stdin.readlines())))
