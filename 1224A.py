import sys
import pickle
import numpy as np
from re import search
from urllib.parse import urljoin
from urllib.parse import urlparse
from urllib.request import Request
from urllib.request import urlopen
from html.parser import HTMLParser
from queue import Queue

class iParser(HTMLParser):
	def __init__(self):
		HTMLParser.__init__(self)
		self.links = []
	def clear_links(self):
		self.links = []
	def handle_starttag(self, tag, attrs):
		if(tag == 'a' and attrs[0][0] == 'href' and attrs[0][1] != '#'):
			self.links.append(attrs[0][1])

class Identifier:
	def __init__(self):
		self.cnt = 0
		self.lst = []
		self.dct = dict()
	def idx(self, x):
		if not x in self.dct:
			self.dct[x] = self.cnt
			self.lst.append(x)
			self.cnt += 1
		return self.dct[x]
	def nam(self, x):
		return self.lst[x]

def find_link(url):
	try:
		Parser = iParser()
		r = Request(url, headers={'User-agent': 'Mozilla 5.10'})
		t = urlopen(r, timeout = 10)
		Parser.clear_links()
		Parser.feed(str(t.read(), encoding = "utf8"))
		txt = Parser.links
	except:
		txt = []
	else:
		pass
	return txt

def LDparse(url, level):
	loc = urlparse(url).netloc
	mat = search("(\.[^.]*){"+str(level)+"}", loc)
	if mat != None:
		return mat.group()
	else:
		return None

def LDmatch(ua, ub, level):
	a = LDparse(ua, level)
	b = LDparse(ub, level)
	return a == b and a != None

def type_accept(url):
	filter_list = ["rar", "pdf", "jpg", "gif", "wmv", "mp3"]
	for suf in filter_list:
		if url.endswith(suf):
			return False
	return True

url = "http://scse.buaa.edu.cn/"

def bfs(start, level):
	ret = dict()
	que = Queue()
	que.put((start, 0))
	ret[start] = dict()
	usd = set()
	while not que.empty():
		now = que.get()
		print("bfs at", now, file = sys.stderr)
		if now[1] > level:
			break
		lst = find_link(now[0])
		for lnk in lst:
			flnk = urljoin(now[0], lnk)
			if (not flnk in usd) and LDmatch(now[0], flnk, 3) and type_accept(flnk):
				que.put((flnk, now[1]+1))
				usd.add(flnk)
				ret[flnk] = dict()
			ret[now[0]][flnk] = ret[now[0]].get(flnk, 0)+1

	return ret

try:
	f = open("table.dict", "rb")
	table = pickle.load(f)
except:
	table = bfs(url, 2)
	f = open("table.dict", "wb")
	pickle.dump(table, f)

#print(table)
nonempty = set()
ider = Identifier()
for i in table:
	if table[i] != dict():
		ider.idx(i)
		nonempty.add(i)

N = ider.cnt
#print(N)
S = np.array([[0.0 for i in range(N)] for i in range(N)])

for i in nonempty:
	tot = 0
	for j in table[i]:
		if j in nonempty:
			x = ider.idx(i)
			y = ider.idx(j)
			tot += table[i][j]
			S[x][y] = table[i][j]
	for j in table[i]:
		if j in nonempty:
			x = ider.idx(i)
			y = ider.idx(j)
			S[x][y] /= tot

S = S.transpose()
alpha = 0.9
eps = 1e-3
K = 20
#print(S)
A = alpha*S+(1-alpha)/N*np.array([[1 for i in range(N)] for i in range(N)])
#print(A)
#print(S.transpose()[ider.idx(url)])
ans = dict()

Pnow = np.array([[0 for i in range(N)]]).transpose()
Plst = np.array([[0 for i in range(N)]]).transpose()
Pnow[ider.idx(url)][0] = 1
while np.linalg.norm(Pnow-Plst) >= eps:
	#print(np.linalg.norm(Pnow-Plst))
	Plst = Pnow
	Pnow = np.matmul(A, Plst)
	#print(Pnow)
	#print("sum = ", sum(Pnow.transpose()[0]))
ans = Pnow.transpose()[0]

#print("sum =", sum(ans))

pr = [(ider.nam(i), ans[i]) for i in range(N)]
pr = sorted(pr, key = lambda x: x[1], reverse = True)
for i in range(K):
	print(pr[i])

