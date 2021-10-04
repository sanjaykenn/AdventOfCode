from collections import defaultdict

import sympy


def main(inp):
	commands = list(map(str.split, inp.rstrip('\n').split('\n')))
	registers = defaultdict(int, {'a': 1})

	def get_value(x):
		try:
			return int(x)
		except ValueError:
			return registers[x]

	i = 0
	while i < 8:
		command, *args = commands[i]
		if command == 'set':
			registers[args[0]] = get_value(args[1])
		elif command == 'sub':
			registers[args[0]] -= get_value(args[1])
		elif command == 'mul':
			registers[args[0]] *= get_value(args[1])
		elif command == 'jnz':
			if get_value(args[0]) != 0:
				i += get_value(args[1])
				continue

		i += 1

	h = 0
	steps = -int(commands[-2][2])
	for b in range(registers['b'], registers['c'] + steps, steps):
		if not sympy.isprime(b):
			h += 1

	return h


if __name__ == '__main__':
	import sys
	print(main(''.join(sys.stdin.readlines())))
