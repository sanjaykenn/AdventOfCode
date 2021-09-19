import itertools
import math
import re


def main(inp):
	shop = '''Weapons:    Cost  Damage  Armor
Dagger        8     4       0
Shortsword   10     5       0
Warhammer    25     6       0
Longsword    40     7       0
Greataxe     74     8       0

Armor:      Cost  Damage  Armor
Leather      13     0       1
Chainmail    31     0       2
Splintmail   53     0       3
Bandedmail   75     0       4
Platemail   102     0       5

Rings:      Cost  Damage  Armor
Damage +1    25     1       0
Damage +2    50     2       0
Damage +3   100     3       0
Defense +1   20     0       1
Defense +2   40     0       2
Defense +3   80     0       3'''.split('\n\n')
	player_health = 100

	re_option = re.compile('^.*?\\s\\s+(\\d+)\\s\\s+(\\d+)\\s\\s+(\\d+)')
	re_boss = re.compile('''^Hit Points: (\\d+)\nDamage: (\\d+)\nArmor: (\\d+)''')

	def parse_category(s):
		result = []
		for line in s.split('\n')[1:]:
			result.append(list(map(int, re_option.match(line).groups())))

		return result

	weapons, armor, rings = map(parse_category, shop)

	class Entity:
		def __init__(self, health, damage, armor):
			self.health = health
			self.damage = damage
			self.armor = armor

	def battle(e1, e2):
		if e1.damage <= e2.armor:
			e1_rounds = math.inf
		else:
			e1_rounds = math.ceil(e2.health / (e1.damage - e2.armor))

		if e2.damage <= e1.armor:
			e2_rounds = math.inf
		else:
			e2_rounds = math.ceil(e1.health / (e2.damage - e1.armor))

		if e1_rounds == e2_rounds == math.inf:
			return True

		return e1_rounds <= e2_rounds

	boss = Entity(*map(int, re_boss.match(inp).groups()))

	def possible_choices(choices, counts):
		for c in counts:
			yield from itertools.combinations(choices, r=c)

	cost = 0
	for choice in itertools.product(possible_choices(weapons, [1]), possible_choices(armor, [0, 1]), possible_choices(rings, [0, 1, 2])):
		damage = sum(map(lambda a: sum(map(lambda b: b[1], a)), choice))
		armor = sum(map(lambda a: sum(map(lambda b: b[2], a)), choice))

		player = Entity(player_health, damage, armor)

		if not battle(player, boss):
			cost = max(cost, sum(map(lambda a: sum(map(lambda b: b[0], a)), choice)))

	return cost


if __name__ == '__main__':
	import sys
	print(main(''.join(sys.stdin.readlines())))
