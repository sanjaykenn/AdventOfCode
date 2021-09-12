def main(inp):
	def simulate(moves):
		x = 0
		y = 0
		visited = {(0, 0)}
		for direction in moves:
			if direction == '>':
				x += 1
			elif direction == '<':
				x -= 1
			elif direction == '^':
				y -= 1
			elif direction == 'v':
				y += 1

			visited.add((x, y))

		return visited

	return len(simulate(inp[:-1:2]) | simulate(inp[1:-1:2]))


if __name__ == '__main__':
	import sys
	print(main(''.join(sys.stdin.readlines())))
