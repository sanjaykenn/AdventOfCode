import re


def main(inp):
	re_vowels = re.compile('[aeiou]')
	re_double = re.compile('(.)\\1')
	blacklist = ['ab', 'cd', 'pq', 'xy']
	count = 0

	for line in inp[:-1].split('\n'):
		if len(re_vowels.findall(line)) >= 3 and re_double.search(line):
			try:
				next(filter(lambda b: b in line, blacklist))
			except StopIteration:
				count += 1

	return count


if __name__ == '__main__':
	import sys

	print(main(''.join(sys.stdin.readlines())))
