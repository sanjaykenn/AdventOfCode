def main(inp):
	opp, my = zip(*map(str.split, inp.splitlines()))

	opp = (ord(choice) - ord('A') for choice in opp)
	my = (ord(choice) - ord('X') + 1 for choice in my)

	return sum((a - b) % 3 * 3 + a for a, b in zip(my, opp))


if __name__ == '__main__':
	import sys
	print(main(''.join(sys.stdin.readlines())))
