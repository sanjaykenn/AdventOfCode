def main(inp):
	state = 'group'
	score = 0
	for c in inp.rstrip('\n'):
		if state == 'garbage':
			if c == '>':
				state = 'group'
			elif c == '!':
				state = 'ignore'
			else:
				score += 1
		elif state == 'ignore':
			state = 'garbage'
		elif state == 'group':
			if c == '<':
				state = 'garbage'

	return score


if __name__ == '__main__':
	import sys
	print(main(''.join(sys.stdin.readlines())))
