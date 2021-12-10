from collections import deque


def main(inp):
	result = 0
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
				result += {
					')': 3,
					']': 57,
					'}': 1197,
					'>': 25137
				}[c]
				break

	return result


if __name__ == '__main__':
	import sys
	print(main(''.join(sys.stdin.readlines())))
