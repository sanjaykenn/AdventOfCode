def main(inp):
	steps = int(inp)
	position = 0
	result = None

	for i in range(1, 5000001):
		position = (position + steps) % i + 1
		if position == 1:
			result = i

	return result


if __name__ == '__main__':
	import sys
	print(main(''.join(sys.stdin.readlines())))
