def main(inp):
	days = [0] * 9
	for day in map(int, inp.rstrip().split(',')):
		days[day] += 1

	for day in range(81):
		days[(day + 6) % 9] += days[(day + 8) % 9]

	return sum(days)


if __name__ == '__main__':
	import sys

	print(main(''.join(sys.stdin.readlines())))
