def main(inp):
	def get_even_division(a):
		for i in range(len(a)):
			for j in range(len(a)):
				if i != j and a[i] % a[j] == 0:
					return a[i] // a[j]

	return sum(map(
		get_even_division,
		map(
			lambda line: list(map(int, line.split())),
			inp.rstrip('\n').split('\n')
		)
	))


if __name__ == '__main__':
	import sys
	print(main(''.join(sys.stdin.readlines())))
