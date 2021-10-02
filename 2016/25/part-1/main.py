def main(inp):
	commands = list(map(str.split, inp.rstrip('\n').split('\n')))
	registers = {'a': 0, 'b': 0, 'c': 0, 'd': 0}

	def get_value(a):
		try:
			return int(a)
		except ValueError:
			return registers[a]

	i = 0
	while i < 8:
		command, *args = commands[i]

		if command == 'cpy':
			value, register = args
			if register in registers:
				registers[register] = get_value(value)
		elif command == 'inc':
			register, = args
			if register in registers:
				registers[register] += 1
		elif command == 'dec':
			register, = args
			if register in registers:
				registers[register] -= 1
		elif command == 'jnz':
			condition, jump = map(get_value, args)
			if condition != 0:
				i += jump
				continue

		i += 1

	d = registers['d']
	return int(2/3 * 4**(int((3*d / 2) ** 0.25) - 1)) - d


if __name__ == '__main__':
	import sys
	print(main(''.join(sys.stdin.readlines())))
