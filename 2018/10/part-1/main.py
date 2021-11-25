import re


class Light:
	def __init__(self, x, y, vx, vy):
		self.x, self.y, self.vx, self.vy = x, y, vx, vy

	def move(self):
		self.x += self.vx
		self.y += self.vy
		return self

	def distance_to(self, other):
		return abs(self.x - other.x) + abs(self.y - other.y)

	def copy(self):
		return Light(self.x, self.y, self.vx, self.vy)

	def __lt__(self, other):
		return (self.y, self.x) < (other.y, other.x)


def main(inp):
	r = re.compile('position=<([- ]\\d+), ([- ]\\d+)> velocity=<([- ]\\d+), ([- ]\\d+)>')
	lights = []
	for line in inp.splitlines():
		lights.append(Light(*map(int, r.match(line).groups())))

	size = min(lights).distance_to(max(lights))
	while True:
		new_lights = [light.copy().move() for light in lights]
		new_size = min(new_lights).distance_to(max(new_lights))
		if new_size < size:
			lights = new_lights
			size = new_size
		else:
			top_left = min(lights)
			bottom_right = max(lights)
			x1 = top_left.x
			y1 = top_left.y
			x2 = bottom_right.x
			y2 = bottom_right.y
			field = [['.'] * (x2 - x1 + 1) for _ in range(y1, y2 + 1)]

			for light in lights:
				field[light.y - y1][light.x - x1] = '#'

			print('\n'.join([''.join(row) for row in field]))
			break


if __name__ == '__main__':
	import sys
	print(main(''.join(sys.stdin.readlines())))
