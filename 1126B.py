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
def dfs(x):
	usd.add(x)
	print(x, end = " ")
	for now in node[x]:
		now = now[0]
		if not now in usd:
			dfs(now)
dfs(start)
print()

