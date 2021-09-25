import re


def main(inp):
	re_goes = re.compile('^value (\\d+) goes to bot (\\d+)$')
	re_give = re.compile('^bot (\\d+) gives low to ([a-z]+) (\\d+) and high to ([a-z]+) (\\d+)$')
	bots = {}
	give_commands = []

	for line in inp.rstrip('\n').split('\n'):
		m = re_goes.match(line)
		if m is not None:
			value, bot = map(int, m.groups())
			bots[bot] = bots.get(bot, ()) + (value, )
			continue

		m = re_give.match(line)
		if m is not None:
			bot_give, id1, out1, id2, out2 = m.groups()
			bot_give = int(bot_give)
			out1 = int(out1)
			out2 = int(out2)
			give_commands.append((bot_give, id1, out1, id2, out2))

	while True:
		for bot_give, id1, out1, id2, out2 in give_commands:
			if len(bots.get(bot_give, ())) != 2:
				continue

			low, high = sorted(bots[bot_give])

			if low == 17 and high == 61:
				return bot_give

			bots[bot_give] = ()
			if id1 == 'bot':
				bots[out1] = bots.get(out1, ()) + (low, )

			if id2 == 'bot':
				bots[out2] = bots.get(out2, ()) + (high, )


if __name__ == '__main__':
	import sys
	print(main(''.join(sys.stdin.readlines())))
