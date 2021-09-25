import hashlib
import itertools


def main(inp):
	prefix = inp.rstrip('\n')
	password = [None] * 8
	count = 0

	for i in itertools.count():
		h = hashlib.md5(f'{prefix}{i}'.encode()).hexdigest()
		if h.startswith('00000'):
			position = int(h[5], 16)

			if 0 <= position < 8 and password[position] is None:
				password[position] = h[6]
				count += 1
				if count >= 8:
					return ''.join(password)


if __name__ == '__main__':
	import sys
	print(main(''.join(sys.stdin.readlines())))
