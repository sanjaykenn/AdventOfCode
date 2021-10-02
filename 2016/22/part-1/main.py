import itertools
import re


def main(inp):
	re_node = re.compile('^[^ ]* +\\d+T +(\\d+)T +(\\d+)T +\\d+%$')
	nodes = []

	for line in inp.rstrip('\n').split('\n')[2:]:
		nodes.append(tuple(map(int, re_node.match(line).groups())))

	def is_pair(a, b):
		return 0 < a[0] <= b[1]

	count = 0
	for node_a, node_b in itertools.combinations(nodes, r=2):
		if is_pair(node_a, node_b) or is_pair(node_b, node_a):
			count += 1

	return count


if __name__ == '__main__':
	import sys
	print(main(''.join(sys.stdin.readlines())))
