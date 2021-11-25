import numpy as np


def get_sum(sum_field, x1, y1, x2, y2):
	value = sum_field[y2 - 1, x2 - 1] + sum_field[y1 - 1, x1 - 1]
	value -= sum_field[y1 - 1, x2 - 1]
	value -= sum_field[y2 - 1, x1 - 1]

	return value


def main(inp):
	grid_serial_number = int(inp)
	field = np.zeros((301, 301), int)

	for y in range(1, field.shape[0]):
		for x in range(1, field.shape[1]):
			rack_id = x + 10
			power_level = rack_id * (rack_id * y + grid_serial_number) // 100 % 10 - 5
			field[y, x] = power_level

	field_sum = field.cumsum(1).cumsum(0)
	best_sum = -float('inf')
	result = None
	for size in range(1, min(field.shape)):
		for y in range(1, field.shape[0] - size):
			for x in range(1, field.shape[1] - size):
				s = get_sum(field_sum, x, y, x + size, y + size)
				if best_sum < s:
					best_sum = s
					result = f'{x},{y},{size}'

	return result


if __name__ == '__main__':
	import sys
	print(main(''.join(sys.stdin.readlines())))
