class SQueue(object):
	def __init__(self, init_len=8):
		self.__elem = [0] * init_len
		self.__len = init_len
		self.__head = 0
		self.__num = 0


	def __extend(self):
		old_len = self.__len
		self.__len *= 2
		new_elems = [0] * self.__len
		for i in range(old_len):
			new_elems[i] = self.__elem[(self.__head + i) % old_len]
		self.__elem, self.__head = new_elems, 0


	def is_empty(self):
		return self.__num == 0


	def peek(self):
		if self.__num == 0:
			raise QueueUnderflow
		return self.__elem[self.__head]
		

	def enqueue(self, e):
		if self.__num == self.__len:
			self.__extend()
		self.__elem[(self.__head + self.__num) % self.__len] = e
		self.__num += 1
		
		
	def dequeue(self):
		if self.__num == 0:
			raise QueueUnderflow
		e = self.__elem[self.__head]
		self.__head = (self.__head + 1) % self.__len
		self.__num -= 1
		return e

class Stack(object):
	def __init__(self):
		self.av = SQueue()
		self.bv = SQueue()

	def push(self, x):
		self.bv.enqueue(x)

	def pop(self):
		if self.av.is_empty() and self.bv.is_empty():
			return None
		elif self.bv.is_empty():
			while not self.av.is_empty():
				self.bv.enqueue(self.av.dequeue())
		while not self.bv.is_empty():
			x = self.bv.dequeue()
			if self.bv.is_empty():
				return x
			else :
				self.av.enqueue(x)
	def empty(self):
		return self.av.is_empty() and self.bv.is_empty()

N = int(input())
stk = Stack()
out1 = []
out2 = []
flag = True
for i in range(N):
	a = input()
	stk.push(a)

M = int(input())
for i in range(M):
	a, *b = input().split()
	if a == 'A':
		stk.push(*b)
	else:
		c = stk.pop()
		if c == None:
			flag = False
			break
		else:
			out1.append(c)

if flag:
	while not stk.empty():
		out2.append(stk.pop())
	print(" ".join(out1))
	print(" ".join(out2))
else:
	print("No")
