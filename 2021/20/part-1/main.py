import itertools
from collections import defaultdict

import numpy as np


def get_area_value(image, x, y):
	return sum(1 << (8 - a) for a in range(9) if image[a // 3 + y - 1, a % 3 + x - 1])


def enhance_image(input_image, enhancer, default_value):
	output = defaultdict(lambda: default_value)
	y_min, y_max = min(map(lambda a: a[0], input_image)), max(map(lambda a: a[0], input_image))
	x_min, x_max = min(map(lambda a: a[1], input_image)), max(map(lambda a: a[1], input_image))

	for y, x in itertools.product(range(y_min - 2, y_max + 3), range(x_min - 2, x_max + 3)):
		if enhancer[get_area_value(input_image, x, y)] != default_value:
			output[y, x] = not default_value

	return output


def main(inp):
	enhancer, image = inp.rstrip('\n').split('\n\n')
	enhancer = np.array(list(enhancer)) == '#'
	y, x = np.where(np.array([list(line) for line in image.splitlines()]) == '#')
	image = defaultdict(bool, {(y, x): True for y, x in zip(y, x)})

	image = enhance_image(image, enhancer, True)
	image = enhance_image(image, enhancer, False)

	return sum(image.values())


if __name__ == '__main__':
	import sys
	print(main(''.join(sys.stdin.readlines())))
