import sys
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

ans = bfs(url, 2)
print(ans)

