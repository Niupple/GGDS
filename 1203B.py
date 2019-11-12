dist = dict()
inf = 10**9

line = list(map(int, input().split()))
N = len(line)

for i in range(N):
	if(line[i] != -1):
		dist[(0, i)] = line[i]
	else:
		dist[(0, i)] = inf

for i in range(1, N):
	line = list(map(int, input().split()))
	for j in range(0, N):
		if(line[j] != -1):
			dist[(i, j)] = line[j]
		elif(i != j):
			dist[(i, j)] = inf
		else:
			dist[(i, j)] = 0

for k in range(N):
	for i in range(N):
		for j in range(N):
			dist[(i, j)] = min(dist[(i, k)]+dist[(k, j)], dist[(i, j)])

s, t = input().split()
s = ord(s)-ord('A')
t = ord(t)-ord('A')

print(dist[(s, t)])
