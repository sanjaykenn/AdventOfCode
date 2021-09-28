import itertools
import re
from collections import deque


def main(inp):
	commands = inp.rstrip('\n').split('\n')

	re_swap_position = re.compile('^swap position (\\d+) with position (\\d+)$')
	re_swap_letter = re.compile('^swap letter ([a-z]) with letter ([a-z])$')
	re_rotate_left = re.compile('^rotate left (\\d+) steps?$')
	re_rotate_right = re.compile('^rotate right (\\d+) steps?$')
	re_rotate_based = re.compile('^rotate based on position of letter ([a-z])$')
	re_reverse = re.compile('^reverse positions (\\d+) through (\\d+)$')
	re_move = re.compile('^move position (\\d+) to position (\\d+)$')

	def scramble(s):
		s = deque(s)
		for line in commands:
			m = re_swap_position.match(line)
			if m:
				x, y = map(int, m.groups())
				s[x], s[y] = s[y], s[x]
				continue

			m = re_swap_letter.match(line)
			if m:
				x, y = m.groups()
				a, b = map(s.index, (x, y))
				s[a] = y
				s[b] = x
				continue

			m = re_rotate_left.match(line)
			if m:
				x = int(m.group(1))
				s.rotate(-x)
				continue

			m = re_rotate_right.match(line)
			if m:
				x = int(m.group(1))
				s.rotate(x)
				continue

			m = re_rotate_based.match(line)
			if m:
				x = s.index(m.group(1))
				x += 1 if x < 4 else 2
				s.rotate(x)
				continue

			m = re_reverse.match(line)
			if m:
				x, y = map(int, m.groups())
				s = list(s)
				s[x:y + 1] = reversed(s[x:y + 1])
				s = deque(s)
				continue

			m = re_move.match(line)
			if m:
				x, y = map(int, m.groups())
				a = s[x]
				del s[x]
				s.insert(y, a)
				continue

		return ''.join(s)

	for password in itertools.permutations('abcdefgh'):
		if scramble(password) == 'fbgdceah':
			return ''.join(password)


if __name__ == '__main__':
	import sys
	print(main(''.join(sys.stdin.readlines())))
