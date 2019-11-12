from queue import Queue
cnt = 0
idx = dict()
node = dict()

def get_id(x):
	global cnt
	if not x in idx:
		cnt += 1
		idx[x] = cnt
	return idx[x]

def add_edge(f, t):
	if not f in node:
		node[f] = [t]
	else:
		node[f].append(t)

N, start = input().split()
N = int(N)

for i in range(N):
	line = input()
	ns = line[line.index("{")+1:line.index("}")].strip()
	f = (line[0])
	ns = ns.split(",")
	for j in ns:
		j = j.strip().split(":")
		add_edge(f, (j[0], int(j[-1])))

usd = set()
def bfs(x):
	que = Queue()
	que.put(x)
	while not que.empty():
		now = que.get()
		if not now in usd:
			usd.add(now)
			print(now, end = " ")
			for nxt in node[now]:
				nxt = nxt[0]
				if not nxt in usd:
					que.put(nxt)
bfs(start)
print()

