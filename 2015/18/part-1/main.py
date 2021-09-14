import numpy as np


def main(inp):
	lights = np.array(list(map(list, inp[:-1].split('\n')))) == '#'

	def is_on(x, y):
		if x < 0 or y < 0 or x >= lights.shape[1] or y >= lights.shape[0]:
			return False

		return lights[y, x]

	def count_neighbors(x, y):
		count = 0

		for y1 in range(y - 1, y + 2):
			for x1 in range(x - 1, x + 2):
				if x == x1 and y == y1:
					continue
				elif is_on(x1, y1):
					count += 1

		return count

	for _ in range(100):
		new_lights = np.zeros_like(lights, dtype=bool)
		for y in range(new_lights.shape[0]):
			for x in range(new_lights.shape[1]):
				if is_on(x, y):
					if count_neighbors(x, y) in {2, 3}:
						new_lights[y, x] = True
				else:
					if count_neighbors(x, y) == 3:
						new_lights[y, x] = True

		lights = new_lights

	return np.sum(lights)


if __name__ == '__main__':
	import sys
	print(main(''.join(sys.stdin.readlines())))
