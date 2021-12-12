import re

from graph import Graph


def dfs(g, start, end='end', visited=None, double=True):
	if start == end:
		return 1

	visited = visited or set()
	if start.lower() == start:
		visited.add(start)

	path_count = 0
	for _, node, _ in g.edges(from_node=start):
		if node not in visited:
			path_count += dfs(g, node, visited=visited.copy(), double=double)
		elif double and node != 'start':
			path_count += dfs(g, node, visited=visited.copy(), double=False)

	return path_count


def main(inp):
	g = Graph()

	for line in inp.splitlines():
		a, b = line.split('-')
		g.add_edge(a, b, bidirectional=True)

	return dfs(g, 'start')


if __name__ == '__main__':
	import sys
	print(main(''.join(sys.stdin.readlines())))
