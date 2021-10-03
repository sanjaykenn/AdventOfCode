from collections import deque


def main(inp):
	programs = deque(list(map(chr, range(ord('a'), ord('p') + 1))))
	count = 1_000_000_000
	start = programs.copy()
	history = deque()

	for i in range(count):
		if i > 0 and programs == start:
			return ''.join(history[count % i])

		history.append(programs.copy())
		for command in inp.rstrip('\n').split(','):
			if command[0] == 's':
				programs.rotate(int(command[1:]))
			elif command[0] == 'x':
				i1, i2 = map(int, command[1:].split('/'))
				programs[i1], programs[i2] = programs[i2], programs[i1]
			elif command[0] == 'p':
				i1, i2 = map(programs.index, command[1:].split('/'))
				programs[i1], programs[i2] = programs[i2], programs[i1]

	return ''.join(programs)


if __name__ == '__main__':
	import sys
	print(main(''.join(sys.stdin.readlines())))
