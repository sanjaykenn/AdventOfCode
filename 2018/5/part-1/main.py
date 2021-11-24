import string


def main(inp):
	polymer = inp.rstrip('\n')
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
			return len(polymer)


if __name__ == '__main__':
	import sys
	print(main(''.join(sys.stdin.readlines())))
