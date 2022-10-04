import itertools
import operator
from collections import deque

OVERLAP_COUNT = 12


def rotations(scanner):
	for i in range(3):
		x, y, z = [j % 3 for j in range(i, i + 3)]

		yield {(pos[x], pos[y], pos[z]) for pos in scanner}
		yield {(pos[x], -pos[y], -pos[z]) for pos in scanner}
		yield {(-pos[x], pos[y], -pos[z]) for pos in scanner}
		yield {(-pos[x], -pos[y], pos[z]) for pos in scanner}

		yield {(-pos[x], -pos[z], -pos[y]) for pos in scanner}
		yield {(-pos[x], pos[z], pos[y]) for pos in scanner}
		yield {(pos[x], -pos[z], pos[y]) for pos in scanner}
		yield {(pos[x], pos[z], -pos[y]) for pos in scanner}


def shift(a, p1):
	p1 = tuple(p1)
	return {tuple(map(operator.add, p1, p2)) for p2 in a}


def find_match(a, b):
	for p in itertools.product(a, b):
		new_beacons = shift(b, map(operator.sub, *p))
		if len(a & new_beacons) >= OVERLAP_COUNT:
			return new_beacons


def sq_distance(a, b):
	return sum([(x - y)**2 for x, y in zip(a, b)])


def square_distances(a):
	return {sq_distance(x, y) for x, y in itertools.combinations(a, 2)}


def main(inp):
	scanners = [{tuple(map(int, beacon.split(','))) for beacon in scanner.splitlines()[1:]} for scanner in inp.split('\n\n')]
	beacons = scanners[0]
	scanners_left = deque(range(len(scanners) - 1))
	rotated_scanners = [list(rotations(scanner)) for scanner in scanners[1:]]
	beacons_square_distances = square_distances(beacons)
	scanner_square_distances = deque([square_distances(scanner) for scanner in scanners[1:]])

	last_match = 0
	overlapping_distances = 66

	while scanners_left:
		index = scanners_left[0]

		if len(scanner_square_distances[index] & beacons_square_distances) >= overlapping_distances:
			for scanner in rotated_scanners[index]:
				new_beacons = find_match(beacons, scanner)
				if new_beacons is not None:
					beacons |= new_beacons
					scanners_left.popleft()
					beacons_square_distances |= {sq_distance(a, b) for a, b in itertools.product(beacons, new_beacons)}
					last_match = 0
					break
			else:
				last_match += 1
				if last_match >= len(scanners_left):
					last_match = 0
					overlapping_distances -= 1

				scanners_left.rotate(-1)
		else:
			last_match += 1
			if last_match >= len(scanners_left):
				last_match = 0
				overlapping_distances -= 1

			scanners_left.rotate(-1)

	return len(beacons)


if __name__ == '__main__':
	import sys
	print(main(''.join(sys.stdin.readlines())))
