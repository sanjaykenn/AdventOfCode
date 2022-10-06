import itertools


def main(inp):
	lefts = set()
	downs = set()
	inp = inp.splitlines()
	for y, line in enumerate(inp):
		for x, cell in enumerate(line):
			if cell == '>':
				lefts.add((x, y))
			elif cell == 'v':
				downs.add((x, y))

	width = len(inp[0])
	height = len(inp)

	for step in itertools.count(1):
		changed = False
		new_lefts = set()
		new_downs = set()

		for x, y in lefts:
			new_x = (x + 1) % width
			if (new_x, y) in lefts or (new_x, y) in downs:
				new_lefts.add((x, y))
			else:
				new_lefts.add((new_x, y))
				changed = True

		lefts = new_lefts

		for x, y in downs:
			new_y = (y + 1) % height
			if (x, new_y) in lefts or (x, new_y) in downs:
				new_downs.add((x, y))
			else:
				new_downs.add((x, new_y))
				changed = True

		downs = new_downs

		if not changed:
			return step


if __name__ == '__main__':
	import sys
	print(main(''.join(sys.stdin.readlines())))
