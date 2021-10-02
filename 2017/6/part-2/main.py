import itertools

import numpy as np


def main(inp):
	banks = np.array(list(map(int, inp.rstrip('\n').split())))
	visited = {tuple(banks): 0}

	for cycle in itertools.count(1):
		bank = banks.argmax()
		bank_value = banks[bank]
		banks[bank] = 0
		banks += bank_value // len(banks)
		bank2 = (bank + bank_value % len(banks)) % len(banks)
		if bank2 < bank:
			banks[bank + 1:] += 1
			banks[:bank2 + 1] += 1
		else:
			banks[bank + 1:bank2 + 1] += 1

		b = tuple(banks)
		if b in visited:
			return cycle - visited[b]
		else:
			visited[b] = cycle


if __name__ == '__main__':
	import sys
	print(main(''.join(sys.stdin.readlines())))
