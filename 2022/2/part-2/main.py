def main(inp):
	opp, result = zip(*map(str.split, inp.splitlines()))

	opp = (ord(choice) - ord('A') for choice in opp)
	result = (ord(r) - ord('X') for r in result)

	return sum(r * 3 + (r + b + 2) % 3 + 1 for r, b in zip(result, opp))


if __name__ == '__main__':
	import sys
	print(main(''.join(sys.stdin.readlines())))
