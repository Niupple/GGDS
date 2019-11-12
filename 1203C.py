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
		else:
			dist[(i, j)] = inf

t = ord(input())-ord('A')
minn = inf
minp = 0
for i in range(N):
	if(i != t and dist[(i, t)] < minn):
		minn = dist[(i, t)]
		minp = i

print(chr(minp+ord('A')))

