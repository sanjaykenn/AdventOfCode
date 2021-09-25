def main(inp):
	data = list(zip(*inp.rstrip('\n').split('\n')))
	return ''.join(map(lambda d: max(d, key=lambda c: d.count(c)), data))



if __name__ == '__main__':
	import sys
	print(main(''.join(sys.stdin.readlines())))
