import re


def main(inp):
	row, col = map(int, re.match(
		'^To continue, please consult the code grid in the manual\\.  Enter the code at row (\\d+), column (\\d+)\\.',
		inp
	).groups())

	index = int(0.5*row*row + (col - 1.5)*row + 0.5*col*col - 0.5*col + 1)

	value = 20151125
	for _ in range(1, index):
		value = (value * 252533) % 33554393

	return value



if __name__ == '__main__':
	import sys
	print(main(''.join(sys.stdin.readlines())))
