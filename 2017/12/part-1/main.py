import re

import graph


def main(inp):
	re_entry = re.compile('^(\\d+) <-> (.*)$')
	g = graph.Graph()

	for line in inp.rstrip('\n').split('\n'):
		a, b = re_entry.match(line).groups()
		for c in b.split(', '):
			g.add_edge(a, c, bidirectional=True)

	for component in g.components():
		if '0' in component:
			return len(component)


if __name__ == '__main__':
	import sys
	print(main(''.join(sys.stdin.readlines())))
