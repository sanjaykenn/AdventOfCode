import re


class Reindeer:
	def __init__(self, speed, stamina, pause):
		self.speed = speed
		self.stamina = stamina
		self.pause = pause
		self.distance = 0
		self.current_stamina = stamina

	def get_distance(self):
		return self.distance

	def move(self):
		if self.current_stamina > 0:
			self.distance += self.speed
			self.current_stamina -= 1

			if self.current_stamina == 0:
				self.current_stamina = -self.pause
		elif self.current_stamina < 0:
			self.current_stamina += 1

			if self.current_stamina == 0:
				self.current_stamina = self.stamina


def main(inp):
	r = re.compile('^.* can fly (\\d*) km/s for (\\d*) seconds, but then must rest for (\\d*) seconds\\.$')
	reindeer = []

	for line in inp[:-1].split('\n'):
		reindeer.append(Reindeer(*map(int, r.match(line).groups())))

	for second in range(2503):
		for rd in reindeer:
			rd.move()

	return max(map(Reindeer.get_distance, reindeer))


if __name__ == '__main__':
	import sys
	print(main(''.join(sys.stdin.readlines())))
