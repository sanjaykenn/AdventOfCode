def main(inp):
	state = 'group'
	score = 0
	depth = 0
	for c in inp.rstrip('\n'):
		if state == 'garbage':
			if c == '>':
				state = 'group'
			elif c == '!':
				state = 'ignore'
		elif state == 'ignore':
			state = 'garbage'
		elif state == 'group':
			if c == '<':
				state = 'garbage'
			elif c == '{':
				depth += 1
				score += depth
			elif c == '}':
				depth -= 1

	return score


if __name__ == '__main__':
	import sys
	print(main(''.join(sys.stdin.readlines())))
