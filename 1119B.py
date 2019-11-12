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

def dfs(now, mid, pre):
	if now == None:
		return
	pre.append(now.data)
	dfs(now.left, mid, pre)
	mid.append(now.data)
	dfs(now.right, mid, pre)

T = readin()
K = int(input())
root = T[0]
mid = []
pre = []

dfs(root, mid, pre)
print(mid[K-1])
print(" ".join(pre))

