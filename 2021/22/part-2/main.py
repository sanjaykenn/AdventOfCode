import itertools
import re


class Cuboid:
	def __init__(self, x1, x2, y1, y2, z1, z2):
		self.x1 = x1
		self.x2 = x2
		self.y1 = y1
		self.y2 = y2
		self.z1 = z1
		self.z2 = z2

	def intersection(self, other):
		def intersection_1d(a1, a2, b1, b2):
			if b1 <= a1 <= b2 or a1 <= b1 <= a2:
				return max(a1, b1), min(a2, b2)

		x = intersection_1d(self.x1, self.x2, other.x1, other.x2)
		y = intersection_1d(self.y1, self.y2, other.y1, other.y2)
		z = intersection_1d(self.z1, self.z2, other.z1, other.z2)

		if None not in (x, y, z):
			return Cuboid(*x, *y, *z)

	def volume(self):
		return (self.x2 - self.x1 + 1) * (self.y2 - self.y1 + 1) * (self.z2 - self.z1 + 1)

	def subtract(self, other):
		intersection = self.intersection(other)
		if intersection is None:
			yield self
			return

		if self.x1 < intersection.x1:
			yield Cuboid(self.x1, intersection.x1 - 1, self.y1, self.y2, self.z1, self.z2)

		if intersection.x2 < self.x2:
			yield Cuboid(intersection.x2 + 1, self.x2, self.y1, self.y2, self.z1, self.z2)

		if self.y1 < intersection.y1:
			yield Cuboid(intersection.x1, intersection.x2, self.y1, intersection.y1 - 1, self.z1, self.z2)

		if intersection.y2 < self.y2:
			yield Cuboid(intersection.x1, intersection.x2, intersection.y2 + 1, self.y2, self.z1, self.z2)

		if self.z1 < intersection.z1:
			yield Cuboid(intersection.x1, intersection.x2, intersection.y1, intersection.y2, self.z1, intersection.z1 - 1)

		if intersection.z2 < self.z2:
			yield Cuboid(intersection.x1, intersection.x2, intersection.y1, intersection.y2, intersection.z2 + 1, self.z2)

	def __hash__(self):
		return hash((self.x1, self.x2, self.y1, self.y2, self.z1, self.z2))

	def __eq__(self, other):
		return vars(self) == vars(other)


def main(inp):
	r = re.compile('^([a-z]+) x=(-?\\d+)\\.\\.(-?\\d+),y=(-?\\d+)\\.\\.(-?\\d+),z=(-?\\d+)\\.\\.(-?\\d+)$')
	cubes = set()

	for line in inp.splitlines():
		state, *coords = r.match(line).groups()
		cube = Cuboid(*map(int, coords))
		if state == 'on':
			cube = cube,
			for c1 in cubes:
				cube = itertools.chain(*(c2.subtract(c1) for c2 in cube))
			cubes |= set(cube)
		elif state == 'off':
			cubes = set().union(*(c1.subtract(cube) for c1 in cubes))

	return sum(map(Cuboid.volume, cubes))


if __name__ == '__main__':
	import sys
	print(main(''.join(sys.stdin.readlines())))
