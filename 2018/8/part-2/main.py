def get_root_value(nodes):
	nodes = iter(nodes)
	children = next(nodes)
	metadata_count = next(nodes)
	children_values = [get_root_value(nodes) for _ in range(children)]
	metadata = [next(nodes) for _ in range(metadata_count)]

	if len(children_values) <= 0:
		return sum(metadata)
	else:
		result = 0
		for m in metadata:
			if 1 <= m <= len(children_values):
				result += children_values[m - 1]

		return result


def main(inp):
	nodes = map(int, inp.rstrip('\n').split(' '))
	return get_root_value(nodes)


if __name__ == '__main__':
	import sys
	print(main(''.join(sys.stdin.readlines())))
