import itertools
import re


def main(inp):
	player_positions = list(map(int, re.match('^Player 1 starting position: (\\d)\nPlayer 2 starting position: (\\d)$', inp).groups()))
	player_scores = [0] * len(player_positions)
	player_turn = 0

	for i in itertools.count(1, 3):
		if any(player >= 1000 for player in player_scores):
			return (i - 1) * min(player_scores)

		player_positions[player_turn] = (player_positions[player_turn] + 3*i + 2) % 10 + 1
		player_scores[player_turn] += player_positions[player_turn]
		player_turn = (player_turn + 1) % len(player_positions)


if __name__ == '__main__':
	import sys
	print(main(''.join(sys.stdin.readlines())))
