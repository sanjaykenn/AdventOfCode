from collections import deque


def main(inp):
	results = deque()
	for line in inp.splitlines():
		brackets = deque()
		for c in line:
			if c in '([{<':
				brackets.append({
					'(': ')',
					'[': ']',
					'{': '}',
					'<': '>',
				}[c])
			elif c != brackets.pop():
				break
		else:
			score = 0
			for b in reversed(brackets):
				score *= 5
				score += {
					')': 1,
					']': 2,
					'}': 3,
					'>': 4
				}[b]

			results.append(score)

	return sorted(results)[len(results) // 2]


if __name__ == '__main__':
	import sys
	print(main(''.join(sys.stdin.readlines())))
