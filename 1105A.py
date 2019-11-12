class BinTNode:
	def __init__(self, data=-1, left=None, right=None):
		self.data = data
		self.left = left
		self.right = right

def printt(now, ret):
	if now != None and now.data != "None":
		ret.append(now.data)
		printt(now.left, ret)
		printt(now.right, ret)

av = input().split()
N = len(av)
bv = list(map(BinTNode, av))
head = 1
for i in range(N):
	if av[i] != "None" and head < N:
		bv[i].left = bv[head]
		head += 1
		if head == N: break
		bv[i].right = bv[head]
		head += 1
out = []
printt(bv[0], out)
print(" ".join(out))

