def main(inp):
	elves = list(range(int(inp)))

	while len(elves) > 1:
		if len(elves) & 1:
			elves = elves[1::2]
		else:
			elves = elves[::2]

	return elves[0] + 1


if __name__ == '__main__':
	import sys
	print(main(''.join(sys.stdin.readlines())))
