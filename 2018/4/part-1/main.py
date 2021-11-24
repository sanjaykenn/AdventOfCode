import re
from collections import defaultdict

import numpy as np


def main(inp):
	re_row = re.compile('^\\[(\\d+)-(\\d+)-(\\d+) (\\d+):(\\d+)] (.*)$')

	log = []
	for line in inp.rstrip('\n').split('\n'):
		*time, message = re_row.match(line).groups()
		log.append((tuple(map(int, time)), message.split()))

	log = list(sorted(log))
	guard = None
	fell_asleep = None
	midnight_schedule = defaultdict(lambda: np.zeros(60, dtype=int))

	for time, message in log:
		if message[0] == 'Guard':
			guard = int(message[1][1:])
		elif message[0] == 'falls':
			if time[-2] == 23:
				fell_asleep = 0
			else:
				fell_asleep = time[-1]
		elif message[0] == 'wakes':
			if time[-2] == 0:
				midnight_schedule[guard][fell_asleep:time[-1]] += 1

	sleepiest_guard = max(midnight_schedule, key=lambda g: np.sum(midnight_schedule[g]))
	most_asleep_hour = np.argmax(midnight_schedule[sleepiest_guard])

	return sleepiest_guard * most_asleep_hour


if __name__ == '__main__':
	import sys
	print(main(''.join(sys.stdin.readlines())))
