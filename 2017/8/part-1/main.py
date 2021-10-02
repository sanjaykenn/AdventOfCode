import re


def main(inp):
	re_command = re.compile('^([a-z]+) ([a-z]+) (-?\\d+) if ([a-z]+) ([<>=!]+) (-?\\d+)$')
	registers = {}

	for line in inp.rstrip('\n').split('\n'):
		r1, cmd, d, r2, comp, v = re_command.match(line).groups()
		if cmd == 'inc':
			d = int(d)
		elif cmd == 'dec':
			d = -int(d)

		if comp == '>':
			f = lambda a, b: a > b
		elif comp == '<':
			f = lambda a, b: a < b
		elif comp == '>=':
			f = lambda a, b: a >= b
		elif comp == '<=':
			f = lambda a, b: a <= b
		elif comp == '==':
			f = lambda a, b: a == b
		elif comp == '!=':
			f = lambda a, b: a != b

		if f(registers.get(r2, 0), int(v)):
			registers[r1] = registers.get(r1, 0) + int(d)

	return max(registers.values())


if __name__ == '__main__':
	import sys
	print(main(''.join(sys.stdin.readlines())))
