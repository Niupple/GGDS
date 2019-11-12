class BinTNode:
	def __init__(self, data=-1, left=None, right=None):
		self.data = data
		self.left = left
		self.right = right

def readin():
	av = input().split()
	N = len(av)
	bv = list(map(BinTNode, av))
	head = 1
	for i in range(N):
		if av[i] != "None" and head < N:
			if av[head] == "None":
				bv[head] = None
			bv[i].left = bv[head]
			head += 1
			if head == N: break
			if av[head] == "None":
				bv[head] = None
			bv[i].right = bv[head]
			head += 1
	return bv

depth = dict()
father = dict()
node = dict()
T = []
maxd = 0

def dfs(now, f):
	global maxd
	if now == None:
		return
	depth[now] = depth[f]+1
	maxd = max(maxd, depth[now])
	father[now] = f
	node[now.data] = now
	#print("!!", now.data, " depth", depth[now])
	dfs(now.left, now)
	dfs(now.right, now)

def lca(a, b):
	if depth[a] < depth[b]:
		a, b = b, a
	while depth[a] > depth[b]:
		a = father[a]
	while a != b:
		a = father[a]
		b = father[b]
	return a.data

#main
T = readin()
root = T[0]
depth[root] = 0
dfs(root, root)
print(maxd)
