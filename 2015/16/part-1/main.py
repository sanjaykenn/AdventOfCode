import re


def main(inp):
	profile = {
		'children': 3,
		'cats': 7,
		'samoyeds': 2,
		'pomeranians': 3,
		'akitas': 0,
		'vizslas': 0,
		'goldfish': 5,
		'trees': 3,
		'cars': 2,
		'perfumes': 1

	}

	re_profile = re.compile('([a-zA-Z]*): (\\d+)')

	for i, line in enumerate(inp[:-1].split('\n')):
		profile2 = re_profile.findall(line)
		b = True

		for key, value in profile2:
			if profile[key] != int(value):
				b = False
				break

		if b:
			return i + 1


if __name__ == '__main__':
	import sys
	print(main(''.join(sys.stdin.readlines())))
