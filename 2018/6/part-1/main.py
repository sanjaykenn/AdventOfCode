def find_closest_point(x, y, points):
	best_distance = float('inf')
	best_point = None
	for i, (x1, y1) in enumerate(points):
		d = abs(x - x1) + abs(y - y1)
		if d < best_distance:
			best_distance = d
			best_point = i
		elif d == best_distance:
			best_point = None

	return best_point


def main(inp):
	points = [tuple(map(int, line.split(', '))) for line in inp.splitlines()]

	border_left = min(map(lambda p: p[0], points))
	border_right = max(map(lambda p: p[0], points))
	border_top = min(map(lambda p: p[1], points))
	border_bottom = max(map(lambda p: p[1], points))

	finites = set(range(len(points)))

	for i, y in enumerate(range(border_top, border_bottom + 1)):
		finites.discard(find_closest_point(border_left, y, points))
		finites.discard(find_closest_point(border_right, y, points))

	for i, x in enumerate(range(border_left, border_right + 1)):
		finites.discard(find_closest_point(x, border_top, points))
		finites.discard(find_closest_point(x, border_bottom, points))

	results = {point: 0 for point in range(len(points))}

	for y in range(border_top + 1, border_bottom):
		for x in range(border_left + 1, border_right):
			closest = find_closest_point(x, y, points)
			if closest is not None:
				results[find_closest_point(x, y, points)] += 1

	return max([results[i] for i in finites])


if __name__ == '__main__':
	import sys
	print(main(''.join(sys.stdin.readlines())))
