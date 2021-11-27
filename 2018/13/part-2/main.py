class Cart:
	field = None

	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.d = '^>v<'.index(Cart.field[y][x])
		self.next_intersection_turn = 0
		Cart.field[y][x] = '|-|-'[self.d]

	def move(self):
		self.x += [0, 1, 0, -1][self.d]
		self.y += [-1, 0, 1, 0][self.d]

		if Cart.field[self.y][self.x] == '/':
			self.d = [1, 0, 3, 2][self.d]
		if Cart.field[self.y][self.x] == '\\':
			self.d = [3, 2, 1, 0][self.d]
		elif Cart.field[self.y][self.x] == '+':
			self.d = (self.d + [3, 0, 1][self.next_intersection_turn]) % 4
			self.next_intersection_turn = (self.next_intersection_turn + 1) % 3


def main(inp):
	Cart.field = list(map(list, inp.splitlines()))
	carts = {}

	for y, row in enumerate(Cart.field):
		for x, cell in enumerate(row):
			if cell in '^>v<':
				carts[y, x] = Cart(x, y)

	while len(carts) > 1:
		for py, px in sorted(carts.copy()):
			if (py, px) not in carts:
				continue

			cart = carts[py, px]
			cart.move()
			del carts[py, px]

			if (cart.y, cart.x) in carts:
				del carts[cart.y, cart.x]
			else:
				carts[cart.y, cart.x] = cart

	cart = min(carts.values())
	return f'{cart.x},{cart.y}'


if __name__ == '__main__':
	import sys
	print(main(''.join(sys.stdin.readlines())))
