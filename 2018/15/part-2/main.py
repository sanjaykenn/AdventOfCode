import itertools


class Character:
	def __init__(self, hp=200, attack=3):
		self.hp = hp
		self.attack = attack

	def __repr__(self):
		return f'Character({self.hp}, {self.attack})'


class Battle:
	def __init__(self, walls, elves, goblins):
		self.walls = walls
		self.elves = elves
		self.goblins = goblins

	def is_free(self, x, y):
		return (y, x) not in self.walls and (y, x) not in self.elves and (y, x) not in self.goblins

	def breadth_first_search(self, x, y, is_free=None):
		is_free = is_free or self.is_free

		visited = set()
		positions = {(y, x): []}
		while positions:
			new_positions = {}
			for y1, x1 in positions:
				for x2, y2 in [(x1, y1 - 1), (x1 - 1, y1), (x1 + 1, y1), (x1, y1 + 1)]:
					if (y2, x2) not in visited and is_free(x2, y2):
						new_positions[y2, x2] = positions[y1, x1] + [(y1, x1)]
						visited.add((y2, x2))

			yield from sorted(new_positions.items())
			positions = new_positions

	def get_next_move(self, x, y):
		enemies = self.elves if (y, x) in self.goblins else self.goblins

		for (y1, x1), path in self.breadth_first_search(x, y, is_free=lambda x, y: self.is_free(x, y) or (y, x) in enemies):
			if (y1, x1) in enemies:
				return path[1][::-1] if len(path) > 1 else (x, y)

		return x, y

	def move(self, x, y):
		characters = self.elves if (y, x) in self.elves else self.goblins
		x1, y1 = self.get_next_move(x, y)

		if (x, y) == (x1, y1):
			return x, y

		characters[y1, x1] = characters[y, x]
		del characters[y, x]
		return x1, y1

	def attack(self, x, y):
		enemies = self.elves if (y, x) in self.goblins else self.goblins
		character = self.elves.get((y, x), self.goblins.get((y, x)))
		enemy_of_choice = None
		enemy_position = None

		for y1, x1 in [(y - 1, x), (y, x - 1), (y, x + 1), (y + 1, x)]:
			if (y1, x1) in enemies:
				if enemy_of_choice is None or enemy_of_choice.hp > enemies[y1, x1].hp:
					enemy_of_choice = enemies[y1, x1]
					enemy_position = y1, x1

		if enemy_of_choice is None:
			return

		enemy_of_choice.hp -= character.attack

		if enemy_of_choice.hp <= 0:
			del enemies[enemy_position]

	def turn(self, x, y):
		self.attack(*self.move(x, y))

	def all_turns(self):
		for y, x in sorted(self.elves | self.goblins):
			if (y, x) in self.elves or (y, x) in self.goblins:
				self.turn(x, y)

	def no_elves_die(self):
		elves_count = len(self.elves)

		for round_id in itertools.count():
			self.all_turns()
			if not self.elves or not self.goblins:
				if len(self.elves) == elves_count:
					return round_id * sum(elf.hp for elf in self.elves.values())
				else:
					return None

	@staticmethod
	def from_field(field, elves_hp=200, elves_attack=3, goblins_hp=200, goblins_attack=3):
		walls = set()
		elves = {}
		goblins = {}

		for y, row in enumerate(field.splitlines()):
			for x, cell in enumerate(row):
				if cell == '#':
					walls.add((y, x))
				elif cell == 'E':
					elves[y, x] = Character(elves_hp, elves_attack)
				elif cell == 'G':
					goblins[y, x] = Character(goblins_hp, goblins_attack)

		return Battle(walls, elves, goblins)

	def __str__(self):
		entities = self.walls | self.elves.keys() | self.goblins.keys()
		height = max([e[0] for e in entities]) + 1
		width = max([e[1] for e in entities]) + 1
		field = [['.'] * width for _ in range(height)]

		for y in range(height):
			for x in range(width):
				if (y, x) in self.walls:
					field[y][x] = '#'
				elif (y, x) in self.goblins:
					field[y][x] = 'G'
				elif (y, x) in self.elves:
					field[y][x] = 'E'

		return '\n'.join(map(''.join, field))


def main(inp):
	for elves_attack in itertools.count(4):
		result = Battle.from_field(inp, elves_attack=elves_attack).no_elves_die()
		if result is not None:
			return result


if __name__ == '__main__':
	import sys
	print(main(''.join(sys.stdin.readlines())))
