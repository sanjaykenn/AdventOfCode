import heapq
import re

import numpy as np


class Particle:
	def __init__(self, pos, vel, acc):
		self.pos = pos
		self.vel = vel
		self.acc = acc

	def get_at_time(self, t):
		return self.pos + (self.vel + self.acc / 2) * t + self.acc * t * t / 2

	def collides_at_time(self, particle, t):
		return np.all(self.get_at_time(t) == particle.get_at_time(t))

	def collides(self, particle):
		a = (self.acc - particle.acc) / 2
		b = self.vel - particle.vel + a
		c = self.pos - particle.pos

		for i in range(len(a)):
			r = b[i]*b[i] - 4*a[i]*c[i]
			if r < 0:
				return
			elif a[i] == 0:
				if b[i] != 0:
					t = -c[i] / b[i]
					if self.collides_at_time(particle, t):
						return t
				elif c[i] == 0:
					return
			elif not (a[i] == b[i] == c[i] == 0):
				t1, t2 = (-b[i] - np.sqrt(r)) / (2*a[i]), (-b[i] + np.sqrt(r)) / (2*a[i])
				if t1 >= 0 and t1 % 1 == 0 and self.collides_at_time(particle, t1):
					return t1
				elif t2 >= 0 and t2 % 1 == 0 and self.collides_at_time(particle, t2):
					return t2
				else:
					return


def main(inp):
	re_particle = re.compile(
		'^p=<(-?\\d+),(-?\\d+),(-?\\d+)>, v=<(-?\\d+),(-?\\d+),(-?\\d+)>, a=<(-?\\d+),(-?\\d+),(-?\\d+)>$'
	)
	particles = []
	collisions = []
	for line in inp.rstrip('\n').split('\n'):
		p = re_particle.match(line).groups()
		particles.append(Particle(
			np.array(list(map(int, p[:3]))),
			np.array(list(map(int, p[3:6]))),
			np.array(list(map(int, p[6:])))
		))

	for i in range(len(particles)):
		for j in range(i + 1, len(particles)):
			t = particles[i].collides(particles[j])
			if t:
				heapq.heappush(collisions, (t, i, j))

	leftover_particles = set(range(len(particles)))
	while collisions:
		t = collisions[0][0]
		new_leftover_particles = leftover_particles.copy()

		while collisions and collisions[0][0] == t:
			_, p1, p2 = heapq.heappop(collisions)
			if p1 in leftover_particles and p2 in leftover_particles:
				new_leftover_particles.discard(p1)
				new_leftover_particles.discard(p2)

		leftover_particles = new_leftover_particles

	return len(leftover_particles)


if __name__ == '__main__':
	import sys
	print(main(''.join(sys.stdin.readlines())))
