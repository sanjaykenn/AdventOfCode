def main(inp):
	commands = list(map(str.split, inp.rstrip('\n').split('\n')))
	registers = {'a': 12, 'b': 0, 'c': 0, 'd': 0}

	def get_value(a):
		try:
			return int(a)
		except ValueError:
			return registers[a]

	i = 0
	while i < len(commands):
		if i == 3:
			registers['a'] = registers['b'] * registers['d']
			registers['c'] = 0
			registers['d'] = 0
			i = 10

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
		elif command == 'tgl':
			index = i + get_value(args[0])

			if index >= len(commands):
				i += 1
				continue

			replacements = {'inc': 'dec', 'dec': 'inc', 'tgl': 'inc', 'jnz': 'cpy', 'cpy': 'jnz'}

			if commands[index][0] in replacements:
				commands[index][0] = replacements[commands[index][0]]

		i += 1

	return registers['a']


if __name__ == '__main__':
	import sys
	print(main(''.join(sys.stdin.readlines())))
