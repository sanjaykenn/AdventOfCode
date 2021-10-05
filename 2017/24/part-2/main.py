import itertools

from graph import Graph


def main(inp):
	g = Graph()
	g.add_node(0, {'visited': False, 'values': (0,)})

	for v, i in zip(map(lambda line: tuple(map(int, line.split('/'))), inp.rstrip('\n').split('\n')), itertools.count(1)):
		g.add_node(i, {'visited': False, 'values': tuple(set(v))})

	for i in range(len(g.nodes())):
		v1 = g.node(i)['values']
		for j in range(i + 1, len(g.nodes())):
			v2 = g.node(j)['values']
			if set(v1) & set(v2):
				g.add_edge(i, j, bidirectional=True)

	def depth_search(node, side):
		if g.node(node)['visited']:
			return 0, 0

		g.node(node)['visited'] = True
		value = g.node(node)['values'][side]
		result = 0, 0
		for node2 in g.nodes(from_node=node):
			value2 = g.node(node2)['values']
			for side2 in range(len(value2)):
				if value == value2[side2]:
					result = max(result, depth_search(node2, (side2 + 1) % len(value2)))

		g.node(node)['visited'] = False
		return result[0] + 1, result[1] + min(g.node(node)['values']) + max(g.node(node)['values'])

	return depth_search(0, 0)[1]


if __name__ == '__main__':
	import sys
	print(main(''.join(sys.stdin.readlines())))
