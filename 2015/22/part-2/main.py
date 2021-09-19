import re


class Game:
	spells = "Magic Missile", "Drain", "Shield", "Poison", "Recharge"

	def __init__(self, player_health, player_mana, boss_health, boss_damage):
		self.boss_start_damage = boss_damage

		self.player_health = player_health
		self.player_mana = player_mana
		self.boss_health = boss_health
		self.boss_damage = self.boss_start_damage
		self.spent_mana = 0
		self.winner = None

		self.effects = {
			"shield": 0,
			"poison": 0,
			"recharge": 0
		}

	def clone(self):
		game = Game(self.player_health, self.player_mana, self.boss_health, self.boss_start_damage)
		game.boss_damage = self.boss_damage
		game.spent_mana = self.spent_mana
		game.winner = self.winner
		game.effects = self.effects.copy()

		return game

	def _play_effects(self):
		if self.effects["shield"] > 0:
			self.effects["shield"] -= 1
			self.boss_damage = max(1, self.boss_damage - 7)

		if self.effects["poison"] > 0:
			self.effects["poison"] -= 1
			self.boss_health -= 3

		if self.effects["recharge"] > 0:
			self.effects["recharge"] -= 1
			self.player_mana += 101

	def _play_spell(self, price, func):
		if self.player_mana >= price:
			b = func()
			self.player_mana -= price
			self.spent_mana += price

			return True if b is None else b

		return False

	def _magic_missile(self):
		self.boss_health -= 4

	def _drain(self):
		self.boss_health -= 2
		self.player_health += 2

	def _cast_spell(self, s, length):
		if self.effects[s] <= 0:
			self.effects[s] = length
			return True

		return False

	def _set_winner(self):
		if self.boss_health <= 0:
			self.winner = True
		elif self.player_health <= 0:
			self.winner = False

		return self.winner

	def play(self, spell):
		self.player_health -= 1

		if self._set_winner() is not None:
			return

		self._play_effects()

		if spell == "Magic Missile":
			if not self._play_spell(53, self._magic_missile):
				self.winner = False
				return
		elif spell == "Drain":
			if not self._play_spell(73, self._drain):
				self.winner = False
				return
		elif spell == "Shield":
			if not self._play_spell(113, lambda: self._cast_spell("shield", 6)):
				self.winner = False
				return
		elif spell == "Poison":
			if not self._play_spell(173, lambda: self._cast_spell("poison", 6)):
				self.winner = False
				return
		elif spell == "Recharge":
			if not self._play_spell(229, lambda: self._cast_spell("recharge", 5)):
				self.winner = False
				return

		if self._set_winner() is not None:
			return

		self.boss_damage = self.boss_start_damage
		self._play_effects()
		self.player_health -= self.boss_damage

		if self._set_winner() is not None:
			return


def main(inp):
	player_health, player_mana = 50, 500
	boss_health, boss_damage = map(int, re.match('^Hit Points: (\\d+)\nDamage: (\\d+)', inp).groups())

	games = [Game(player_health, player_mana, boss_health, boss_damage)]
	while True:
		for game in games:
			for spell in Game.spells:
				g = game.clone()
				g.play(spell)

				if g.winner is None:
					games.append(g)
				elif g.winner:
					return g.spent_mana


if __name__ == '__main__':
	import sys
	print(main(''.join(sys.stdin.readlines())))
