import re

from graph import Graph


def main(inp):
	r = re.compile('Step (.) must be finished before step (.) can begin\\.')
	g = Graph()
	result = ''

	for line in inp.splitlines():
		a, b = r.match(line).groups()
		g.add_edge(a, b)

	for _ in range(len(g.nodes())):
		node = min(g.nodes(in_degree=0))
		result += node
		g.del_node(node)

	return result


if __name__ == '__main__':
	import sys
	print(main(''.join(sys.stdin.readlines())))
