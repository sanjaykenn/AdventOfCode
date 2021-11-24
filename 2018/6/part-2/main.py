def total_distance(x, y, points):
	return sum([abs(x - x1) + abs(y - y1) for x1, y1, in points])


def main(inp):
	points = [tuple(map(int, line.split(', '))) for line in inp.splitlines()]
	maximum = 10000

	current = {(0, 0): total_distance(0, 0, points)}
	visited = set(current.keys())
	total = int(current[0, 0] < maximum)
	while current:
		new_current = {}
		for x, y in current:
			for dx, dy in [(0, -1), (1, 0), (0, 1), (-1, 0)]:
				x1 = x + dx
				y1 = y + dy
				if (x1, y1) in visited:
					continue

				distance = total_distance(x1, y1, points)

				if distance < maximum:
					new_current[x1, y1] = distance
					visited.add((x1, y1))
					total += 1
				elif distance < current[x, y]:
					new_current[x1, y1] = distance
					visited.add((x1, y1))

		current = new_current

	return total


if __name__ == '__main__':
	import sys
	print(main(''.join(sys.stdin.readlines())))
