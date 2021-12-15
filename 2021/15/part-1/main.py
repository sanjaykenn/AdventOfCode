import networkx as nx
import numpy as np


def main(inp):
	risk = np.array(list(map(list, inp.splitlines())), int)
	g = nx.grid_2d_graph(*risk.shape, create_using=nx.DiGraph)
	return nx.shortest_path_length(g, (0, 0), (risk.shape[0] - 1, risk.shape[1] - 1), lambda n1, n2, e: risk[n2])


if __name__ == '__main__':
	import sys
	print(main(''.join(sys.stdin.readlines())))
