def main(inp):
	n = int(inp)
	recipes = [3, 7]
	elf1 = 0
	elf2 = 1

	while len(recipes) < n + 10:
		recipe = recipes[elf1] + recipes[elf2]
		if recipe < 10:
			recipes.append(recipe)
		else:
			recipes.extend([recipe // 10, recipe % 10])

		elf1 = (elf1 + recipes[elf1] + 1) % len(recipes)
		elf2 = (elf2 + recipes[elf2] + 1) % len(recipes)

	return ''.join(map(str, recipes[n:n+10]))


if __name__ == '__main__':
	import sys
	print(main(''.join(sys.stdin.readlines())))
