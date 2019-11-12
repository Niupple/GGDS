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

def get_id(x) :
	if x >= 0 and x < 10:
		return str(x);
	else:
		return chr(ord('A')+x-10);
	

M, N = input().split()
M = int(M)
N = int(N)
stk = Stack()

x = M
while x != 0:
	stk.push(get_id(x%N))
	x //= N

while not stk.isEmpty():
	print(stk.pop(), end="")

print()
