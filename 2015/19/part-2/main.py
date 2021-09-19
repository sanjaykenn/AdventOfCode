import re


def main(inp):
	re_replacements = re.compile('^(.*) => (.*)$')

	inp = inp[:-1].split('\n')
	medicine = inp[-1]
	replacements = sorted(
		map(re.Match.groups, map(re_replacements.match, inp[:-2])),
		key=lambda a: len(a[1]), reverse=True
	)

	result = 0
	while medicine != 'e':
		for find, replace in replacements:
			if replace in medicine:
				medicine = medicine.replace(replace, find, 1)
				result += 1
				break

	return result


if __name__ == '__main__':
	import sys
	print(main(''.join(sys.stdin.readlines())))
