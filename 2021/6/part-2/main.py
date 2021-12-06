def main(inp):
	days = [0] * 9
	for d in map(int, inp.rstrip('\n').split(',')):
		days[d] += 1

	for day in range(256):
		new_days = [0] * 9
		new_days[8] = days[0]
		new_days[6] = days[0]
		for d in range(8):
			new_days[d] += days[d + 1]

		days = new_days

	return sum(days)


if __name__ == '__main__':
	import sys
	print(main(''.join(sys.stdin.readlines())))
