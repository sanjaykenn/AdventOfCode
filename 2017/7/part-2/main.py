import re


def main(inp):
	re_entry = re.compile('^([^\\s]+) \\((\\d+)\\)( -> (.*))?$')

	nodes = set()
	node_children = set()
	parent_children = {}

	for line in inp.rstrip('\n').split('\n'):
		parent, weight, _, children = re_entry.match(line).groups()
		weight = int(weight)
		nodes.add(parent)

		if children:
			children = set(children.split(', '))
			nodes |= children
			node_children |= children
			parent_children[parent] = weight, children
		else:
			parent_children[parent] = weight, set()

	def get_weight(node):
		weight, children = parent_children[node]
		return weight + sum(map(get_weight, children))

	def get_correct_balance(node):
		n_children = list(parent_children[node][1])
		child_weights = list(map(get_weight, n_children))
		incorrect_weight = min(child_weights, key=child_weights.count)
		if child_weights.count(incorrect_weight) > 1: return

		index = child_weights.index(incorrect_weight)
		value = get_correct_balance(n_children[index])
		if value is None:
			correct_weight = child_weights[0 if index > 0 else 1]
			difference = correct_weight - incorrect_weight
			return parent_children[n_children[index]][0] + difference

		return value

	return get_correct_balance(min(nodes - node_children))


if __name__ == '__main__':
	import sys
	print(main(''.join(sys.stdin.readlines())))
