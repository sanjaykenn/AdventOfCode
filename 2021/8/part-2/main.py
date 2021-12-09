import itertools
import operator

letters = 'abcdefg'
combinations = [dict(zip(letters, combination)) for combination in itertools.permutations(letters)]

digits = [
	set('abcefg'),
	set('cf'),
	set('acdeg'),
	set('acdfg'),
	set('bcdf'),
	set('abdfg'),
	set('abdefg'),
	set('acf'),
	set('abcdefg'),
	set('abcdfg'),
]

digit_sizes = {
	2: [1],
	3: [7],
	4: [4],
	5: [2, 3, 5],
	6: [0, 6, 9],
	7: [8]
}


def get_digit(code):
	for i in digit_sizes.get(len(code), []):
		if code == digits[i]:
			return i


def main(inp):
	result = 0
	for line in inp.splitlines():
		codes_1, codes_2 = map(str.split, line.split(' | '))

		for combination in combinations:
			digits_1 = map(lambda code: get_digit(set(map(combination.get, code))), codes_1)
			digits_2 = [get_digit(set(map(combination.get, code))) for code in codes_2]
			if all(map(lambda d: d is not None, itertools.chain(digits_1, digits_2))):
				# no 'initial' parameter in itertools.accumulate in python 3.7 (using pypy 3.7)
				result += sum(map(
					operator.mul,
					itertools.accumulate(itertools.repeat(10), operator.mul),
					reversed(digits_2)
				))

	return result // 10


if __name__ == '__main__':
	import sys
	print(main(''.join(sys.stdin.readlines())))
