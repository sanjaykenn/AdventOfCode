def main(inp):
	result = 0
	for line in inp.splitlines():
		for code in line.split('|')[1].split():
			if len(code) in {2, 3, 4, 7}:
				result += 1

	return result


if __name__ == '__main__':
	import sys
	print(main(''.join(sys.stdin.readlines())))
