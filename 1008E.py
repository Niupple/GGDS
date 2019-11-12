av = dict()
N = int(input())

def insert(nam, num):
	av[nam] = num

def query(nam):
	return av.get(nam, None)

for i in range(N):
	c = input()
	if c == 'A':
		a, b = input().split()
		insert(a, b)
	else:
		a = input()
		b = query(a)
		if b == None:
			print("NONE")
		else:
			print(b)

