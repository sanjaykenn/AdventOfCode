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

	samples, _ = inp.split('\n\n\n\n')
	samples = [zip(*[map(int, match.groups())] * 4) for match in map(re_samples.match, samples.split('\n\n'))]
	result = 0

	for registers_before, (command, *args), registers_after in samples:
		commands_match = 0
		for func in commands.values():
			registers = list(registers_before)
			func(*args)
			commands_match += tuple(registers) == registers_after

		if commands_match >= 3:
			result += 1

	return result


if __name__ == '__main__':
	import sys
	print(main(''.join(sys.stdin.readlines())))
