import itertools
import re


def main(inp):
	r = re.compile('^(.*) would (.*) (\\d*) happiness units by sitting next to (.*)\\.$')
	relation = {'Sanjay': {}}

	for line in inp[:-1].split('\n'):
		person1, state, points, person2 = r.match(line).groups()

		if state == 'gain':
			points = int(points)
		elif state == 'lose':
			points = -int(points)

		if person1 not in relation:
			relation[person1] = {'Sanjay': 0}
			relation['Sanjay'][person1] = 0

		relation[person1][person2] = points

	def evaluate_result(order):
		return sum(map(
			lambda p: relation[p[0]][p[1]] + relation[p[1]][p[0]],
			zip(order, order[1:])
		)) + relation[order[0]][order[-1]] + relation[order[-1]][order[0]]

	first = min(relation.keys())

	return max(map(
		lambda a: evaluate_result((first, ) + a),
		itertools.permutations(relation.keys() - {first}))
	)


if __name__ == '__main__':
	import sys
	print(main(''.join(sys.stdin.readlines())))
