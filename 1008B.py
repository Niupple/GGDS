class Stack:
	def __init__(self):
		self._elems = []
	def isEmpty(self):
		return self._elems == []
	def top(self):
		if self._elems == []:
			raise Exception('Stack is empty when using top()!')
		else:
			return self._elems[-1]
	def push(self, elem):
		self._elems.append(elem)
	def pop(self):
		if self._elems == []:
			raise Exception('Stack is empty when doing pop()!')
		else:
			return self._elems.pop()
	def size(self):
		return len(self._elems)

stk = Stack()
N = int(input())
tot = 0
while True:
	a = int(input())
	if a == 0:
		break
	else:
		if (not stk.isEmpty()) and stk.top() < a:
			tot -= stk.top()
			stk.pop()
			tot += a
			stk.push(a)
		elif stk.size() < N:
			stk.push(a)
			tot += a

print(tot)
