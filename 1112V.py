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

def pre(now, out):
	if(now == None):
		return
	out.append(now.data)
	pre(now.left, out)
	pre(now.right, out)

def mid(now, out):
	if now == None:
		return
	mid(now.left, out)
	out.append(now.data)
	mid(now.right, out)


T = readin()
root = T[0]
for i in T:
	i.left, i.right = i.right, i.left
out = []
pre(root, out)
print(" ".join(out))

out = []
mid(root, out)
print(" ".join(out))
