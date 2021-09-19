import re


def main(inp):
	re_replacements = re.compile('^(.*) => (.*)$')

	inp = inp[:-1].split('\n')
	medicine = inp[-1]
	replacements = list(map(re.Match.groups, map(re_replacements.match, inp[:-2])))
	collections = set()

	for find, replace in replacements:
		pos = 0
		while True:
			m = re.search(find, medicine[pos:])
			if m is None:
				break

			pos += m.start()
			med = medicine[:pos] + replace + medicine[pos + len(find):]
			pos += 1
			collections.add(med)

	return len(collections)


if __name__ == '__main__':
	import sys
	print(main(''.join(sys.stdin.readlines())))
