def get_metadata_sum(nodes):
	nodes = iter(nodes)
	children = next(nodes)
	metadata_count = next(nodes)
	metadata_sum = sum(get_metadata_sum(nodes) for _ in range(children))
	return metadata_sum + sum(next(nodes) for _ in range(metadata_count))


def main(inp):
	nodes = map(int, inp.rstrip('\n').split(' '))
	return get_metadata_sum(nodes)


if __name__ == '__main__':
	import sys
	print(main(''.join(sys.stdin.readlines())))
