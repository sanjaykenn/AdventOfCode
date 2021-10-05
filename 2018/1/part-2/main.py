def main(inp):
	value = 0
	visited = {value}
	while True:
		for i in map(int, inp.rstrip('\n').split('\n')):
			value += i
			if value in visited:
				return value
			visited.add(value)


if __name__ == '__main__':
	import sys
	print(main(''.join(sys.stdin.readlines())))
