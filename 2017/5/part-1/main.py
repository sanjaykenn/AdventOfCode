import itertools


def main(inp):
	a = list(map(int, inp.rstrip('\n').split('\n')))
	i = 0
	for steps in itertools.count():
		if not (0 <= i < len(a)):
			return steps

		a[i] += 1
		i += a[i] - 1


if __name__ == '__main__':
	import sys
	print(main(''.join(sys.stdin.readlines())))
