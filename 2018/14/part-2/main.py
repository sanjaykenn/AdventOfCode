def main(inp):
	n = list(map(int, list(inp.rstrip('\n'))))
	recipes = [3, 7]
	elf1 = 0
	elf2 = 1

	while True:
		recipe = recipes[elf1] + recipes[elf2]
		if recipe < 10:
			recipes.append(recipe)
		else:
			recipes.append(recipe // 10)
			if recipes[-len(n):] == n:
				return len(recipes) - len(n)

			recipes.append(recipe % 10)

		if recipes[-len(n):] == n:
			return len(recipes) - len(n)

		elf1 = (elf1 + recipes[elf1] + 1) % len(recipes)
		elf2 = (elf2 + recipes[elf2] + 1) % len(recipes)


if __name__ == '__main__':
	import sys
	print(main(''.join(sys.stdin.readlines())))
