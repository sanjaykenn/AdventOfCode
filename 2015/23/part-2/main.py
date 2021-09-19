import re


def main(inp):
	re_param_1 = re.compile('^([a-z]*) (.*)$')
	re_param_2 = re.compile('^([a-z]*) (.*), (.*)$')

	code = inp[:-1].split('\n')
	index = 0
	register = {'a': 1, 'b': 0}

	def get_value(p):
		try:
			return int(p)
		except ValueError:
			return register[p]

	while index < len(code):
		op = code[index]

		m = re_param_2.match(op)
		if m:
			op, param1, param2 = m.groups()

			if op == 'jie':
				if get_value(param1) & 1 == 0:
					index += get_value(param2)
					continue
			elif op == 'jio':
				if get_value(param1) == 1:
					index += get_value(param2)
					continue
		else:
			op, param = re_param_1.match(op).groups()

			if op == 'hlf':
				register[param] //= 2
			elif op == 'tpl':
				register[param] *= 3
			elif op == 'inc':
				register[param] += 1
			elif op == 'jmp':
				index += get_value(param)
				continue

		index += 1

	return register['b']


if __name__ == '__main__':
	import sys
	print(main(''.join(sys.stdin.readlines())))
