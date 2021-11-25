import itertools
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
	for second in itertools.count():
		new_lights = [light.copy().move() for light in lights]
		new_size = min(new_lights).distance_to(max(new_lights))
		if new_size < size:
			lights = new_lights
			size = new_size
		else:
			return second


if __name__ == '__main__':
	import sys
	print(main(''.join(sys.stdin.readlines())))
