import numpy as np


def main(inp):
	grid_serial_number = int(inp)
	field = np.zeros((301, 301), int)

	for y in range(1, field.shape[0]):
		for x in range(1, field.shape[1]):
			rack_id = x + 10
			power_level = rack_id * (rack_id * y + grid_serial_number) // 100 % 10 - 5
			field[y, x] = power_level

	best_sum = -float('inf')
	coordinates = None
	for y in range(1, field.shape[0]):
		for x in range(1, field.shape[1]):
			s = np.sum(field[y:y+3, x:x+3])
			if best_sum < s:
				coordinates = x, y
				best_sum = s

	return ','.join(map(str, coordinates))


if __name__ == '__main__':
	import sys
	print(main(''.join(sys.stdin.readlines())))
