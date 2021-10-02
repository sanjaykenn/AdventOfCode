import re


def main(inp):
	re_entry = re.compile('^([^\\s]+) \\(\\d+\\)( -> (.*))?$')

	nodes = set()
	node_children = set()

	for line in inp.rstrip('\n').split('\n'):
		parent, _, children = re_entry.match(line).groups()
		nodes.add(parent)

		if children:
			children = set(children.split(', '))
			nodes |= children
			node_children |= children

	return min(nodes - node_children)


if __name__ == '__main__':
	import sys
	print(main(''.join(sys.stdin.readlines())))
