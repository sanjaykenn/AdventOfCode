from collections import defaultdict


def main(inp):
	commands = list(map(str.split, inp.rstrip('\n').split('\n')))
	registers = defaultdict(int)

	def get_value(x):
		try:
			return int(x)
		except ValueError:
			return registers[x]

	i = 0
	mul_count = 0
	while i < len(commands):
		command, *args = commands[i]
		if command == 'set':
			registers[args[0]] = get_value(args[1])
		elif command == 'sub':
			registers[args[0]] -= get_value(args[1])
		elif command == 'mul':
			registers[args[0]] *= get_value(args[1])
			mul_count += 1
		elif command == 'jnz':
			if get_value(args[0]) != 0:
				i += get_value(args[1])
				continue

		i += 1

	return mul_count


if __name__ == '__main__':
	import sys
	print(main(''.join(sys.stdin.readlines())))
