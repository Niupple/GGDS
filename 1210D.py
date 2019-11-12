#coding=utf-8
from queue import Queue
class edge:
	def __init__(self):
		self.l = 0
		self.t = 0
		self.n = None

node = dict()
txt = open("bgstations_pinyin.txt", mode = 'r')
cnt = 0
idx = dict()
nam = dict()

def add_edge(f, t, l):
	e = edge()
	e.t = t
	e.l = l
	e.n = node.get(f, None)
	node[f] = e

def get_id(x):
	global cnt
	if(idx.get(x, -1) == -1):
		idx[x] = cnt
		nam[cnt] = x
		cnt += 1
	return idx[x]

L = int(txt.readline())
for i in range(L):
	l, N = list(map(int, txt.readline().split()))
	N = int(N)
	line = []
	for j in range(N):
		p, t = txt.readline().split()
		t = int(t)
		line.append((get_id(p), t))
	for j in range(N-1):
		#print("link between %s and %s in line %s" % (nam[line[j][0]], nam[line[j+1][0]], l))
		add_edge(line[j][0], line[j+1][0], l)
		add_edge(line[j+1][0], line[j][0], l)
	txt.readline()

S = input()
T = input()

father = dict()
fromp = dict()
usd = set()
def dijkstra():
	now = get_id(S)
	que = Queue()
	que.put(now)
	usd.add(now)
	father[now] = now
	fromp[now] = None
	while not que.empty():
		now = que.get()
		#print("bfs at %s" % nam[now])
		if(now == get_id(T)):
			return
		e = node[now]
		while e != None:
			nxt = e.t
			if not nxt in usd:
				usd.add(nxt)
				father[nxt] = now
				fromp[nxt] = e
				que.put(nxt)
			e = e.n

dijkstra()
path = []
x = get_id(T)
while(father[x] != x):
	path.append(fromp[x])
	x = father[x]
path = list(reversed(path))
path.append(edge())
nowl, nows = path[0].l, 1
print(S, end = "")
for i in range(len(path)-1):
	if(path[i].l == path[i+1].l):
		nows += 1
	else:
		print("-%s(%d)-%s" % (nowl, nows, nam[path[i].t]), end = "")
		nowl = path[i+1].l
		nows = 1
print()

