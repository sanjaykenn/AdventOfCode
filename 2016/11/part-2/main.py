import itertools
import re

import numpy as np


class State:
	FLOORS = 4

	def __init__(self, microchips, generators, current_floor=0):
		self.microchips = np.array(microchips)
		self.generators = np.array(generators)
		self.current_floor = current_floor

	def move_floor(self, microchips, generators, d_floor):
		self.microchips[microchips] += d_floor
		self.generators[generators] += d_floor
		self.current_floor += d_floor

	def get_next_states(self):
		result = set()

		if self.current_floor > 0:
			for microchips, generators in self.get_possible_moves():
				state = self.copy()
				state.move_floor(microchips, generators, -1)

				if not state.is_fried():
					result.add(state)

		if self.current_floor < State.FLOORS - 1:
			for microchips, generators in self.get_possible_moves():
				state = self.copy()
				state.move_floor(microchips, generators, 1)

				if not state.is_fried():
					result.add(state)

		return result

	def is_fried(self):
		has_generators = np.zeros(State.FLOORS, dtype=bool)
		for floor in self.generators:
			has_generators[floor] = True

		for i in range(len(self.microchips)):
			if has_generators[self.microchips[i]] and self.microchips[i] != self.generators[i]:
				return True

		return False

	def get_possible_moves(self):
		microchips, = np.where(self.microchips == self.current_floor)
		generators, = np.where(self.generators == self.current_floor)

		return itertools.chain(
			map(lambda m: ([m], []), microchips),
			map(lambda g: ([], [g]), generators),
			map(lambda m: (list(m), []), itertools.combinations(microchips, 2)),
			map(lambda g: ([], list(g)), itertools.combinations(generators, 2)),
			map(lambda mg: ([mg[0]], [mg[1]]), itertools.product(microchips, generators))
		)

	def copy(self):
		return State(self.microchips, self.generators, self.current_floor)

	def is_complete(self):
		return all(self.microchips == State.FLOORS - 1) and all(self.generators == State.FLOORS - 1) and self.current_floor == State.FLOORS - 1

	def __hash__(self):
		return hash((tuple(sorted(zip(self.microchips, self.generators))), self.current_floor))

	def __eq__(self, other):
		return hash(self) == hash(other)


def main(inp):
	re_microchip = re.compile('([a-z]+)-compatible microchip')
	re_generator = re.compile('([a-z]+) generator')

	microchips = {}
	generators = {}

	for i, line in enumerate(inp.rstrip('\n').split('\n')):
		microchips |= {microchip: i for microchip in re_microchip.findall(line)}
		generators |= {generator: i for generator in re_generator.findall(line)}

	microchips = [0, 0] + [microchips[microchip] for microchip in sorted(microchips)]
	generators = [0, 0] + [generators[generator] for generator in sorted(generators)]

	states = {State(microchips, generators)}
	visited = set()

	for step in itertools.count():
		for state in states:
			if state.is_complete():
				return step

		visited |= states
		new_states = set()

		for state in states:
			new_states |= state.get_next_states() - visited

		states = new_states


if __name__ == '__main__':
	import sys
	print(main(''.join(sys.stdin.readlines())))
