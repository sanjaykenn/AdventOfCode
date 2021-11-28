import re


def main(inp):
	re_samples = re.compile(
		'Before: \\[(\\d+), (\\d+), (\\d+), (\\d+)]\n(\\d+) (\\d+) (\\d+) (\\d+)\nAfter:  \\[(\\d+), (\\d+), (\\d+), (\\d+)]'
	)

	commands = {
		'addr': lambda a, b, c: registers.__setitem__(c, registers[a] + registers[b]),
		'addi': lambda a, b, c: registers.__setitem__(c, registers[a] + b),
		'mulr': lambda a, b, c: registers.__setitem__(c, registers[a] * registers[b]),
		'muli': lambda a, b, c: registers.__setitem__(c, registers[a] * b),
		'banr': lambda a, b, c: registers.__setitem__(c, registers[a] & registers[b]),
		'bani': lambda a, b, c: registers.__setitem__(c, registers[a] & b),
		'borr': lambda a, b, c: registers.__setitem__(c, registers[a] | registers[b]),
		'bori': lambda a, b, c: registers.__setitem__(c, registers[a] | b),
		'setr': lambda a, b, c: registers.__setitem__(c, registers[a]),
		'seti': lambda a, b, c: registers.__setitem__(c, a),
		'gtri': lambda a, b, c: registers.__setitem__(c, int(a > registers[b])),
		'gtir': lambda a, b, c: registers.__setitem__(c, int(registers[a] > b)),
		'gtrr': lambda a, b, c: registers.__setitem__(c, int(registers[a] > registers[b])),
		'eqir': lambda a, b, c: registers.__setitem__(c, int(a == registers[b])),
		'eqri': lambda a, b, c: registers.__setitem__(c, int(registers[a] == b)),
		'eqrr': lambda a, b, c: registers.__setitem__(c, int(registers[a] == registers[b]))
	}

	samples, code = inp.split('\n\n\n\n')
	samples = [zip(*[map(int, match.groups())] * 4) for match in map(re_samples.match, samples.split('\n\n'))]
	code = [map(int, row) for row in map(str.split, code.splitlines())]
	possible_opcodes = [set(commands) for _ in range(16)]

	for registers_before, (command, *args), registers_after in samples:
		remove_opcodes = set()
		for opcode in possible_opcodes[command]:
			registers = list(registers_before)
			commands[opcode](*args)
			if tuple(registers) != registers_after:
				remove_opcodes.add(opcode)

		possible_opcodes[command] -= remove_opcodes

	command_to_opcode = [None] * len(possible_opcodes)

	for _ in range(len(command_to_opcode)):
		command = next(filter(lambda i: len(possible_opcodes[i]) == 1, range(len(possible_opcodes))))
		opcode, = possible_opcodes[command]
		command_to_opcode[command] = opcode

		for opcodes in possible_opcodes:
			opcodes.discard(opcode)

	registers = [0] * 4
	for (command, *args) in code:
		commands[command_to_opcode[command]](*args)

	return registers[0]


if __name__ == '__main__':
	import sys
	print(main(''.join(sys.stdin.readlines())))
