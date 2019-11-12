cnt = 0
idx = dict()
node = dict()

def get_id(x):
	global cnt
	if not x in idx:
		idx[x] = cnt
		cnt += 1
	return idx[x]

def add_edge(f, t):
	if not f in node:
		node[f] = [t]
	else:
		node[f].append(t)

N, start = input().split()
N = int(N)
start = get_id(start)
dist = dict()

for i in range(N):
	line = input()
	ns = line[line.index("{")+1:line.index("}")].strip()
	f = get_id(line[0])
	ns = ns.split(",")
	for j in ns:
		j = j.strip().split(":")
		t = get_id(j[0])
		add_edge(f, (t, int(j[-1])))
		dist[(f, t)] = int(j[-1])

maxd = -1

def dis(x, y):
	return dist.get((x, y), 10**9)

def floyd():
	global maxd
	for k in range(N):
		for i in range(N):
			for j in range(N):
				dist[(i, j)] = min(dis(i, k)+dis(k, j), dis(i, j))

floyd()
for i in range(N):
	pa = (start, i)
	if(dist[pa] != 10**9):
		maxd = max(maxd, dist[pa])
print(maxd)

