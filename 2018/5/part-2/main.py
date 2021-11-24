import string


def main(inp):
	best = float('inf')

	for unit in string.ascii_lowercase:
		polymer = inp.rstrip('\n').replace(unit, '').replace(unit.upper(), '')
		replacements = []
		for letter in string.ascii_lowercase:
			replacements.extend([
				f'{letter}{letter.upper()}',
				f'{letter.upper()}{letter}'
			])

		while True:
			t = polymer
			for replacement in replacements:
				polymer = polymer.replace(replacement, '')

			if t == polymer:
				best = min(best, len(polymer))
				break

	return best


if __name__ == '__main__':
	import sys
	print(main(''.join(sys.stdin.readlines())))
