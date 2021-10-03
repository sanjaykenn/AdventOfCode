from collections import defaultdict


def main(inp):
	commands = list(map(str.split, inp.rstrip('\n').split('\n')))
	registers = defaultdict(int)
	send = None

	def get_value(v):
		try:
			return int(v)
		except ValueError:
			return registers[v]

	i = 0
	while i < len(commands):
		command, *args = commands[i]

		if command == 'snd':
			send = get_value(args[0])
		elif command == 'set':
			registers[args[0]] = get_value(args[1])
		elif command == 'add':
			registers[args[0]] += get_value(args[1])
		elif command == 'mul':
			registers[args[0]] *= get_value(args[1])
		elif command == 'mod':
			registers[args[0]] %= get_value(args[1])
		elif command == 'rcv':
			if args[0] != '0':
				return send
		elif command == 'jgz':
			if get_value(args[0]) > 0:
				i += get_value(args[1])
				continue

		i += 1


if __name__ == '__main__':
	import sys
	print(main(''.join(sys.stdin.readlines())))
