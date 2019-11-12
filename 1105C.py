from queue import Queue
class BinTNode:
	def __init__(self, data=-1, left=None, right=None):
		self.data = data
		self.left = left
		self.right = right

def listout(lst, lev, itm):
	if lev >= len(lst):
		lst.append([])
	#print("lev =", lev, "itm =", itm, "len =", len(lst))
	lst[lev].append(itm)

def printt(x, ret):
	que = Queue()
	que.put((x, 0))
	listout(ret, 0, x.data)
	while not que.empty():
		now = que.get()
		#listout(ret, now[1], now[0].data)
		if now[0].left != None and now[0].left.data != "None":
			listout(ret, now[1]+1, now[0].left.data)
			que.put((now[0].left, now[1]+1))
		else:
			listout(ret, now[1]+1, None)

		if now[0].right != None and now[0].right.data != "None":
			listout(ret, now[1]+1, now[0].right.data)
			que.put((now[0].right, now[1]+1))
		else:
			listout(ret, now[1]+1, None)

def dfs(x, ret):
	if x.left != None and x.left.data != "None":
		dfs(x.left, ret)
	if x.right != None and x.right.data != "None":
		dfs(x.right, ret)
	ret.append(x.data)

def sym(x):
	n = len(x)
	for i in range(n):
		if i < n-i-1:
			if x[i] != x[n-i-1]:
				return False
		else:
			break
	return True

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
flag = True
for i in range(len(out)):
	if not sym(out[i]) :
		flag = False;
		break
if flag:
	print("Yes", end = " ")
else:
	print("No", end = " ")
out = []
dfs(bv[0], out)
print(" ".join(out))

