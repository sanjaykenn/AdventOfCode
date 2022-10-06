import re


re_function = re.compile(r'''inp w
mul x 0
add x z
mod x 26
div z (1|26)
add x (-?\d+)
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y (-?\d+)
mul y x
add z y''')


def main(inp):
	all_funcs = re_function.findall(inp)
	stack = []
	result = [None] * len(all_funcs)

	for i, (z, a, b) in enumerate(all_funcs):
		if z == '1':
			stack.append((i, int(b)))
		else:
			a = int(a)
			j, b = stack.pop()
			result[j] = max(1 - a - b, 1)
			result[i] = result[j] + a + b

	return ''.join(map(str, result))


if __name__ == '__main__':
	import sys
	print(main(''.join(sys.stdin.readlines())))
