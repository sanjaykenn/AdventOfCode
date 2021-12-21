import functools
import re


class Universe:
	def __init__(self, player_positions, player_scores=None, player_turn=0):
		self.player_positions = player_positions
		self.player_scores = player_scores or (0,) * len(self.player_positions)
		self.player_turn = player_turn

	def get_winner(self):
		for player in range(len(self.player_scores)):
			if self.player_scores[player] >= 21:
				return player

	@functools.cache
	def get_winner_counts(self):
		winner = self.get_winner()
		wins = [0] * len(self.player_positions)

		if winner is not None:
			wins[winner] = 1
			return wins

		next_turn = (self.player_turn + 1) % len(self.player_scores)
		for dice, mul in zip(range(3, 10), [1, 3, 6, 7, 6, 3, 1]):
			player_positions = list(self.player_positions)
			player_score = list(self.player_scores)
			player_positions[self.player_turn] = (player_positions[self.player_turn] + dice - 1) % 10 + 1
			player_score[self.player_turn] += player_positions[self.player_turn]
			wins = [(a + b * mul) for a, b in zip(wins, Universe(tuple(player_positions), tuple(player_score), next_turn).get_winner_counts())]

		return wins

	def __hash__(self):
		return hash(self.player_positions) ^ hash(self.player_scores) ^ hash(self.player_turn)

	def __eq__(self, other):
		return vars(self) == vars(other)


def main(inp):
	player_positions = tuple(map(int, re.match('^Player 1 starting position: (\\d)\nPlayer 2 starting position: (\\d)$', inp).groups()))
	return max(Universe(player_positions).get_winner_counts())


if __name__ == '__main__':
	import sys
	print(main(''.join(sys.stdin.readlines())))
