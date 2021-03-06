from graph import Graph


def dfs(g, start='start', end='end', visited=None):
	if start == end:
		return 1

	visited = visited or set()
	if start.islower():
		visited.add(start)

	path_count = 0
	for _, node, _ in g.edges(from_node=start):
		if node not in visited:
			path_count += dfs(g, node, visited=visited.copy())

	return path_count


def main(inp):
	g = Graph()

	for line in inp.splitlines():
		a, b = line.split('-')
		g.add_edge(a, b, bidirectional=True)

	return dfs(g)


if __name__ == '__main__':
	import sys
	print(main(''.join(sys.stdin.readlines())))
