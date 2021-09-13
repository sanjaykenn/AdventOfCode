import json


def main(inp):
	storage = json.loads(inp)

	def get_sum(d):
		if type(d) is int:
			return d
		elif type(d) is list:
			return sum(map(get_sum, d))
		elif type(d) is dict:
			return sum(map(get_sum, d.values()))
		else:
			return 0

	return get_sum(storage)


if __name__ == '__main__':
	import sys
	print(main(''.join(sys.stdin.readlines())))
