from queue import Queue
class BinTNode:
	def __init__(self, data=-1, left=None, right=None):
		self.data = data
		self.left = left
		self.right = right

pre = input().split()
mid = input().split()
node = {i: BinTNode(i) for i in pre}
pos = {mid[i] : i for i in range(len(mid))}
N = len(mid)
head = 0
pre.append("")

def build(l, r, x):
	global head
	#print(head, l, r)
	if l > r:
		return None
	elif l == r:
		head += 1
		now = BinTNode(x)
		return now
	head += 1
	m = pos[x]
	now = BinTNode(x)
	now.left = build(l, m-1, pre[head])
	now.right = build(m+1, r, pre[head])
	return now

def bfs(root):
	out = []
	que = Queue()
	que.put((root, 0))
	while not que.empty():
		now = que.get()
		if now[0] != None:
			if now[1] >= len(out):
				out.append([])
			out[now[1]].append(now[0])
			que.put((now[0].left, now[1]+1))
			que.put((now[0].right, now[1]+1))
	H = len(out)
	for i in range(H):
		if i > 0 and i < H-1 and len(out[i]) != 2*len(out[i-1]):
			return False
	return True

Id = dict()
usd = dict()
def dfs(x, f):
	#print("dfs ", x.data if x != None else 0)
	if x == None:
		return
	if x.left != None:
		Id[x.left] = Id[x]*2
		usd[Id[x.left]] = 1
		#print("mark ", Id[x.left])
		dfs(x.left, x)
	if x.right != None:
		Id[x.right] = Id[x]*2+1
		usd[Id[x.right]] = 1
		#print("mark ", Id[x.right])
		dfs(x.right, x)

root = build(0, len(mid)-1, pre[0])
Id[root] = 1
usd[1] = 1
dfs(root, root)
flag = True
for i in range(N):
	if(usd.get(i+1, 0) == 0):
		#print(i+1, "lost")
		flag = False
		break
if flag:
	print("True")
else:
	print("False")

