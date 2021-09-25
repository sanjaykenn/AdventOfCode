import re


def main(inp):
	re_room = re.compile('^([a-z\\-]*)-(\\d*)\\[([a-z]{5})]$')
	real_rooms = 0

	for room in inp.rstrip('\n').split('\n'):
		name, room_id, checksum = re_room.match(room).groups()
		characters = ''.join(map(
			lambda t: t[1],
			sorted(map(
				lambda c: (-name.count(c), c), set(name) - {'-'}
			))
		))

		if checksum == characters[:5]:
			real_rooms += int(room_id)

	return real_rooms


if __name__ == '__main__':
	import sys
	print(main(''.join(sys.stdin.readlines())))
