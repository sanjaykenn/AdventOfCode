import re


def get_pattern(positions, position):
	result = ''
	for p in range(position - 2, position + 3):
		result += '#' if p in positions else '.'

	return result


def main(inp):
	inp = inp.splitlines()
	initial_state = re.match('^initial state: ([#.]*)$', inp[0]).group(1)
	re_spread = re.compile('^([#.]{5}) => ([#.])$')
	spreads = dict([re_spread.match(line).groups() for line in inp[2:]])

	positions = set()
	for position, value in enumerate(initial_state):
		if value == '#':
			positions.add(position)

	for _ in range(20):
		start = min(positions) - 2
		end = max(positions) + 3
		new_positions = set()

		for position in range(start, end):
			if spreads[get_pattern(positions, position)] == '#':
				new_positions.add(position)

		positions = new_positions

	return sum(positions)


if __name__ == '__main__':
	import sys
	print(main(''.join(sys.stdin.readlines())))
