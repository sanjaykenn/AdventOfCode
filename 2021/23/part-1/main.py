import itertools
import re
from collections import deque

re_burrow = re.compile(r'''#############
#[.]{11}#
###([A-D])#([A-D])#([A-D])#([A-D])###
\s\s#([A-D])#([A-D])#([A-D])#([A-D])#
\s\s#########''')


class Burrow:
	COSTS = [1, 10, 100, 1000]
	STEPS = [
		[3, 2, 2, 4, 6, 8, 9],
		[5, 4, 2, 2, 4, 6, 7],
		[7, 6, 4, 2, 2, 4, 5],
		[9, 8, 6, 4, 2, 2, 3]
	]

	def __init__(self, rooms, hall=None, cost=0, offset=None, pop_rooms=True):
		self.rooms = [deque(room) for room in rooms]
		self.hall = list(hall or [None] * (len(self.rooms) + 3))
		self.cost = cost
		self.offset = list(offset or [0] * len(self.rooms))

		if pop_rooms:
			for i, room in enumerate(self.rooms):
				while room and room[-1] == i:
					room.pop()

	def possible_move_outs(self, room):
		if len(self.rooms[room]) <= 0:
			yield from []
		else:
			yield from itertools.takewhile(lambda i: self.hall[i] is None, range(room + 1, -1, -1))
			yield from itertools.takewhile(lambda i: self.hall[i] is None, range(room + 2, len(self.hall)))

	def possible_move_ins(self, room):
		if len(self.rooms[room]) > 0:
			yield from []
		else:
			for i in range(room + 1, -1, -1):
				if self.hall[i] is not None:
					if self.hall[i] == room:
						yield i

					break

			for i in range(room + 2, len(self.hall)):
				if self.hall[i] is not None:
					if self.hall[i] == room:
						yield i

					break

	def apply_all_possible_moves(self):
		for i, (room, offset) in enumerate(zip(self.rooms, self.offset)):
			if len(room) > 0:
				amphipod = room[0]
				for pos in self.possible_move_outs(i):
					cost = (offset + Burrow.STEPS[i][pos]) * Burrow.COSTS[amphipod]
					burrow = Burrow(self.rooms, self.hall, self.cost + cost, self.offset, False)
					burrow.rooms[i].popleft()
					burrow.hall[pos] = amphipod
					burrow.offset[i] += 1
					yield burrow
			else:
				for pos in self.possible_move_ins(i):
					amphipod = self.hall[pos]
					cost = (offset + Burrow.STEPS[i][pos] - 1) * Burrow.COSTS[amphipod]
					burrow = Burrow(self.rooms, self.hall, self.cost + cost, self.offset, False)
					burrow.hall[pos] = None
					burrow.offset[i] -= 1
					yield burrow

	def is_solved(self):
		return all(amphipod is None for amphipod in self.hall) and all(len(room) <= 0 for room in self.rooms)

	def __hash__(self):
		return hash(tuple(tuple(room) for room in self.rooms) + tuple(self.hall) + tuple(self.offset))

	def __eq__(self, other):
		return self.rooms == other.rooms and self.hall == other.hall and self.offset == other.offset


def main(inp):
	amphipods = re_burrow.match(inp).groups()
	burrows = {Burrow([[ord(amphipod) - ord('A') for amphipod in room] for room in zip(amphipods[:4], amphipods[4:])])}
	visited = {burrow: burrow.cost for burrow in burrows}
	best_cost = float('inf')

	while burrows:
		new_burrows = {}
		for burrow in burrows:
			if burrow.cost >= best_cost:
				pass
			elif burrow.is_solved():
				best_cost = burrow.cost
			else:
				for new_burrow in burrow.apply_all_possible_moves():
					if visited.get(new_burrow, float('inf')) > new_burrow.cost:
						visited[new_burrow] = new_burrow.cost

						if new_burrows.get(new_burrow, float('inf')) > new_burrow.cost:
							new_burrows.pop(new_burrow, None)
							new_burrows[new_burrow] = new_burrow.cost

		burrows = new_burrows.keys()

	return best_cost


if __name__ == '__main__':
	import sys
	print(main(''.join(sys.stdin.readlines())))
