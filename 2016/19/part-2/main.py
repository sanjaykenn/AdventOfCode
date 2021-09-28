import heapq
from collections import deque


def main(inp):
	elves = deque(range(int(inp)))
	stealing_elves = []

	i = 0
	while len(elves) > 1:
		if len(stealing_elves) > 0 and i == stealing_elves[0]:
			elves.popleft()
			heapq.heappop(stealing_elves)
		else:
			heapq.heappush(stealing_elves, i + (len(elves) - len(stealing_elves)) // 2)
			elves.rotate(-1)
			i += 1

	return elves[0] + 1


if __name__ == '__main__':
	import sys
	print(main(''.join(sys.stdin.readlines())))
