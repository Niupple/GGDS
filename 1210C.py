class edge:
	def __init__(self):
		self.i = 0
		self.t = 0
		self.n = None

N, M = input().split()
N = int(N)
M = int(M)
node = [None for i in range(N)]

def add_edge(f, t, i):
	e = edge()
	e.i = i
	e.t = t
	e.n = node[f]
	node[f] = e

for i in range(M):
	d, u, v = list(map(int, input().split()))
	add_edge(u, v, d)
	add_edge(v, u, d)

stk = []
usd = set()
ans = []

def dfs(x):
	if x == N-1:
		ans.append(stk[:])
		return
	e = node[x]
	while(e != None):
		now = e.t
		if not now in usd:
			usd.add(now)
			stk.append(e.i)
			dfs(now)
			stk.pop()
			usd.remove(now)
		e = e.n

usd.add(0)
dfs(0)
ans = sorted(ans)
for line in ans:
	for i in range(len(line)):
		line[i] = str(line[i])
	print(" ".join(line))

