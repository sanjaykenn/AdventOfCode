import numpy as np


def main(inp):
	row_count = 400000
	row = np.array(list(inp.rstrip('\n'))) == '.'
	result = np.sum(row)

	for _ in range(row_count - 1):
		new_row = np.zeros_like(row, dtype=bool)
		new_row[0], new_row[-1] = row[1], row[-2]
		new_row[1:-1] = row[:-2] == row[2:]
		row = new_row
		result += np.sum(row)

	return result


if __name__ == '__main__':
	import sys
	print(main(''.join(sys.stdin.readlines())))
