import re


def main(inp):
	commands = [
		(re.compile('^([a-z0-9]+)$'), lambda v: v),
		(re.compile('^NOT ([a-z0-9]+)$'), lambda v: 65535 - v),
		(re.compile('^([a-z0-9]+) AND ([a-z0-9]+)$'), lambda v, w: v & w),
		(re.compile('^([a-z0-9]+) OR ([a-z0-9]+)$'), lambda v, w: v | w),
		(re.compile('^([a-z0-9]+) LSHIFT ([a-z0-9]+)$'), lambda v, w: v << w),
		(re.compile('^([a-z0-9]+) RSHIFT ([a-z0-9]+)$'), lambda v, w: v >> w)
	]

	circuits = {}
	for line in inp[:-1].split('\n'):
		command, output = line.split(' -> ')
		circuits[output] = command

	cache = {}
	def get_value(v):
		if v in cache:
			return cache[v]

		if v.isdigit():
			return int(v)

		for reg, cmd in commands:
			m = reg.match(circuits[v])
			if m is None:
				continue

			values = map(get_value, m.groups())
			out = cmd(*values)
			cache[v] = out
			return out

	return get_value(circuits['a'])


if __name__ == '__main__':
	import sys
	print(main(''.join(sys.stdin.readlines())))
