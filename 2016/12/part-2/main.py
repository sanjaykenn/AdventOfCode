import re


def main(inp):
	re_cpy = re.compile('^cpy (.+) (.+)$')
	re_inc = re.compile('^inc (.+)$')
	re_dec = re.compile('^dec (.+)$')
	re_jnz = re.compile('^jnz (.+) (.+)$')

	commands = inp.rstrip('\n').split('\n')
	registers = {'a': 0, 'b': 0, 'c': 1, 'd': 0}

	def get_value(a):
		try:
			return int(a)
		except ValueError:
			return registers[a]

	i = 0
	while i < len(commands):
		command = commands[i]
		m = re_cpy.match(command)
		if m is not None:
			value, register = m.groups()
			registers[register] = get_value(value)
			i += 1
			continue

		m = re_inc.match(command)
		if m is not None:
			register, = m.groups()
			registers[register] += 1
			i += 1
			continue

		m = re_dec.match(command)
		if m is not None:
			register, = m.groups()
			registers[register] -= 1
			i += 1
			continue

		m = re_jnz.match(command)
		if m is not None:
			condition, jump = map(get_value, m.groups())
			if condition != 0:
				i += jump
			else:
				i += 1
			continue

	return registers['a']


if __name__ == '__main__':
	import sys
	print(main(''.join(sys.stdin.readlines())))
