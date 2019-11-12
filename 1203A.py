edges = []

line = list(map(int, input().split()))
N = len(line)

father = list(range(N))

def find(x):
	if x == father[x]:
		return x
	else:
		father[x] = find(father[x])
		return father[x]

for i in range(N):
	if(line[i] != -1):
		edges.append((line[i], 0, i))

for i in range(1, N):
	line = list(map(int, input().split()))
	for j in range(i+1, N):
		if(line[j] != -1):
			edges.append((line[j], i, j))

E = sorted(edges, key = lambda x : x[0])
ans = 0
for i in E:
	x, y = i[1], i[2]
	if(find(x) != find(y)):
		ans += i[0];
		father[find(x)] = y

print(ans)

