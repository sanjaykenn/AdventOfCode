import itertools
import re

from graph import Graph


def main(inp):
	workers = 5

	r = re.compile('Step (.) must be finished before step (.) can begin\\.')
	g = Graph()
	jobs = {}
	working = set()

	for line in inp.splitlines():
		a, b = r.match(line).groups()
		g.add_edge(a, b)
		jobs[a] = ord(a) - 4
		jobs[b] = ord(b) - 4

	for time in itertools.count():
		if not g.nodes():
			return time

		available = sorted(g.nodes(in_degree=0), key=lambda n: (n not in working, n))
		working |= set(available[:workers])

		for node in available[:workers]:
			jobs[node] -= 1
			if jobs[node] == 0:
				g.del_node(node)
				working.remove(node)


if __name__ == '__main__':
	import sys
	print(main(''.join(sys.stdin.readlines())))
