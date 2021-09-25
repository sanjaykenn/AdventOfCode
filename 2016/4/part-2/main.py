import re


def main(inp):
	re_room = re.compile('^([a-z\\-]*)-(\\d*)\\[([a-z]{5})]$')
	real_rooms = []

	for room in inp.rstrip('\n').split('\n'):
		name, room_id, checksum = re_room.match(room).groups()
		characters = ''.join(map(
			lambda t: t[1],
			sorted(map(
				lambda c: (-name.count(c), c), set(name) - {'-'}
			))
		))

		if checksum == characters[:5]:
			room_id = int(room_id)
			decrypted_name = ''
			for c in name:
				if c == '-':
					decrypted_name += ' '
				else:
					decrypted_name += chr((ord(c) - ord('a') + room_id) % 26 + ord('a'))

			if 'north' in decrypted_name or 'pole' in decrypted_name:
				return room_id

	return real_rooms


if __name__ == '__main__':
	import sys
	print(main(''.join(sys.stdin.readlines())))
