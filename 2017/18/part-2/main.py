from collections import defaultdict, deque


class Program:
	def __init__(self, code, send_queue, recv_queue, program_id):
		self.registers = defaultdict(int)
		self.code = code
		self.send_queue = send_queue
		self.recv_queue = recv_queue
		self.i = 0
		self.count_send = 0
		self.registers['p'] = program_id

	def get_value(self, v):
		try:
			return int(v)
		except ValueError:
			return self.registers[v]

	def run_next(self):
		if self.i >= len(self.code):
			return False

		command, *args = self.code[self.i]

		if command == 'snd':
			self.send_queue.append(self.get_value(args[0]))
			self.count_send += 1
		elif command == 'set':
			self.registers[args[0]] = self.get_value(args[1])
		elif command == 'add':
			self.registers[args[0]] += self.get_value(args[1])
		elif command == 'mul':
			self.registers[args[0]] *= self.get_value(args[1])
		elif command == 'mod':
			self.registers[args[0]] %= self.get_value(args[1])
		elif command == 'rcv':
			if not self.recv_queue:
				return 'waiting'

			self.registers[args[0]] = self.recv_queue.popleft()
		elif command == 'jgz':
			if self.get_value(args[0]) > 0:
				self.i += self.get_value(args[1])
				return True

		self.i += 1
		return True


def main(inp):
	commands = list(map(str.split, inp.rstrip('\n').split('\n')))
	program0 = Program(commands, deque(), deque(), 0)
	program1 = Program(commands, program0.recv_queue, program0.send_queue, 1)

	while True:
		o0 = program0.run_next()
		o1 = program1.run_next()

		if o0 == o1 == 'waiting':
			return program1.count_send


if __name__ == '__main__':
	import sys
	print(main(''.join(sys.stdin.readlines())))
