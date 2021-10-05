import re


def main(inp):
	re_init = re.compile('^Begin in state ([A-Z])\\.\nPerform a diagnostic checksum after (\\d+) steps\\.$')
	re_state = re.compile('''^In state ([A-Z]):
  If the current value is 0:
    - Write the value (\\d)\\.
    - Move one slot to the ([a-z]+)\\.
    - Continue with state ([A-Z])\\.
  If the current value is 1:
    - Write the value (\\d)\\.
    - Move one slot to the ([a-z]+)\\.
    - Continue with state ([A-Z])\\.$''')

	inp = inp.rstrip('\n').split('\n\n')

	state, steps = re_init.match(inp[0]).groups()
	steps = int(steps)
	states = {}

	for line in inp[1:]:
		g = re_state.match(line).groups()
		states[g[0]] = g[1:4], g[4:]

	ones = set()
	position = 0
	for _ in range(steps):
		b = position in ones
		if states[state][b][0] == '1':
			ones.add(position)
		else:
			ones.discard(position)

		position += -1 if states[state][b][1] == 'left' else 1
		state = states[state][b][2]

	return len(ones)


if __name__ == '__main__':
	import sys
	print(main(''.join(sys.stdin.readlines())))
