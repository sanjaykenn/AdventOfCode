from collections import deque


def main(inp):
	steps = int(inp)
	buffer = deque()

	for i in range(2018):
		buffer.rotate(-steps)
		buffer.append(i)

	return buffer[0]


if __name__ == '__main__':
	import sys
	print(main(''.join(sys.stdin.readlines())))
