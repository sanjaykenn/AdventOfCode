def main(inp):
	floor = 0
	for i in range(len(inp)):
		if inp[i] == '(':
			floor += 1
		else:
			floor -= 1

		if floor < 0:
			return i + 1


if __name__ == '__main__':
	import sys
	print(main(''.join(sys.stdin.readlines())))
