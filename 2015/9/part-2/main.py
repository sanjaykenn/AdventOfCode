import itertools
import re

from graph import Graph


def main(inp):
	re_distance = re.compile('^(.*) to (.*) = (\\d*)$')
	g = Graph()

	for line in inp[:-1].split('\n'):
		location1, location2, distance = re_distance.match(line).groups()
		g.add_edge(location1, location2, int(distance), True)

	return max(map(g.distance_from_path, itertools.permutations(g.nodes())))


if __name__ == '__main__':
	import sys
	print(main(''.join(sys.stdin.readlines())))
