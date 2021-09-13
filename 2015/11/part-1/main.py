import re
import string


def main(inp):
	re_two_double = re.compile('^.*(.)\\1.*(.)\\2.*$')
	alphabet = string.ascii_lowercase
	increments = {f'{i}{j}{k}' for i, j, k in zip(alphabet, alphabet[1:], alphabet[2:])}
	forbidden = {'i', 'o', 'l'}

	def increase(s):
		if s[-1] == 'z':
			return increase(s[:-1]) + 'a'

		return s[:-1] + chr(ord(s[-1]) + 1)

	password = inp.rstrip('\n')

	while True:
		if re_two_double.match(password) and\
				any(map(lambda inc: inc in password, increments)) \
				and all(map(lambda f: f not in password, forbidden)):
			return password

		password = increase(password)


if __name__ == '__main__':
	import sys
	print(main(''.join(sys.stdin.readlines())))
