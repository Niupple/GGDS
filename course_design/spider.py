import sys
import pickle
import numpy as np
import re
from re import search
from re import findall
from urllib.parse import urljoin
from urllib.parse import urlparse
from urllib.request import Request
from urllib.request import urlopen
from html.parser import HTMLParser
from queue import Queue
from jieba import cut_for_search

class Artical:
    def __init__(self):
        self.title = ""
        self.content = ""
    def from_html(self, txt):
        # self.content = "\n".join(findall(r"(?<=<p>)[^<>]*(?=</p>)", txt))
        self.title = search(r"(?<=<title>)[^<>]*(?=</title>)", txt).group()
        lines = findall(r"<p[^>]*>[^<>]*</p>", txt)
        for i in range(len(lines)):
            tag = findall(r"<[^>]*>", lines[i])
            for j in tag:
                lines[i] = lines[i].replace(j, "")
        self.content = "\n".join(lines)
        return self

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

def LDparse(url, level):
    loc = "/"+urlparse(url).netloc
    mat = search(r"([./][^.]*){"+str(level)+"}", loc)
    if mat != None:
        return mat.group()
    else:
        return None

def LDmatch(ua, ub, level):
    a = LDparse(ua, level)
    b = LDparse(ub, level)
    return a == b and a != None

class PageType:
    filter_list = ["rar", "pdf", "jpg", "gif", "wmv", "mp3"]
    index_list = []
    NULL = 0
    FILE = 1
    VIDEO = 2
    INDEX = 3
    CONTENT = 4
    OTHERS = 5
    def __init__(self, url = ""):
        self.url = url
        if(url != ""):
            self.type = self.WebType(url)
        else:
            self.type = PageType.NULL
    def WebType(self, url):
        self.url = url
        for suf in PageType.filter_list:
            if url.endswith(suf):
                self.type = PageType.FILE
                return self.type
        path = urlparse(url).path
        if path.endswith("/") or path == "" or search("\bindex\b", url, flags = re.I):
            self.type = PageType.INDEX
        elif search("\bvideo\b", path, flags = re.I):
            self.type = PageType.VIDEO
        else:
            self.type = PageType.CONTENT
        return self.type
    def accept(self):
        return self.type == PageType.INDEX or self.type == PageType.CONTENT

class Webs:
    def __init__(self):
        self.links = dict()
        self.article = dict()
        self.type = dict()

class Spider:
    def __init__(self):
        self.url = ""
        self.filter_list = ["rar", "pdf", "jpg", "gif", "wmv", "mp3"]
        self.webs = Webs()
        self.ider = Identifier()
        self.nonempty = set()
        self.pr = dict()
        self.site_number = 0

    def find_link(self, url):
        try:
            Parser = iParser()
            r = Request(url, headers={'User-agent': 'Mozilla 5.10'})
            t = urlopen(r, timeout = 1)
            Parser.clear_links()
            site = t.read().decode("utf-8")
            article = Artical().from_html(site)
            Parser.feed(site)
            links = Parser.links
        except:
            links = []
            article = Artical()
        else:
            pass
        return (links, article)

    def bfs(self, start, level):
        ret = dict()
        que = Queue()
        usd = set()
        usd.add(start)
        que.put((start, 0))
        ret[start] = dict()
        self.webs.type[start] = PageType(start).type
        while not que.empty():
            now = que.get()
            print("bfs at", now, file = sys.stderr)
            if now[1] > level:
                break
            lst, art = self.find_link(now[0])
            self.webs.article[now[0]] = art
            ret[now[0]] = dict()
            for lnk in lst:
                flnk = urljoin(now[0], lnk)
                tp = PageType(flnk)
                self.webs.type[flnk] = tp.type
                # print("checking ", flnk)
                if (not flnk in usd) and LDmatch(now[0], flnk, 4) and tp.accept():
                    que.put((flnk, now[1]+1))
                    usd.add(flnk)
                ret[now[0]][flnk] = ret[now[0]].get(flnk, 0)+1
        self.webs.links = ret
        return ret

    def get_sites(self, url = "https://news.sina.com.cn/", level = 2):
        self.url = url
        try:
            f = open("webs.class", "rb")
            # ft = open("table.dict", "rb")
            # fa = open("artical.dict", "rb")
            # self.table = pickle.load(ft)
            # self.artical = pickle.load(fa)
            self.webs = pickle.load(f)
        except:
            self.bfs(url, level)
            # ft = open("table.dict", "wb")
            # fa = open("artical.dict", "wb")
            # pickle.dump(self.table, ft)
            # pickle.dump(self.artical, fa)
            f = open("webs.class", "wb")
            pickle.dump(self.webs, f)
        table = self.webs.links
        for i in table:
            if table[i] != dict():
                self.ider.idx(i)
                self.nonempty.add(i)
        return table

    def page_rank(self, alpha = 0.9, eps = 1e-3):
        self.site_number = self.ider.cnt
        # print(self.site_number)
        # print(self.url)
        # print(self.url in self.table)
        # print(self.table[self.url])
        #Constructing S
        table = self.webs.links
        S = np.array([[0.0 for i in range(self.site_number)] for i in range(self.site_number)])
        for i in self.nonempty:
            tot = 0
            for j in table[i]:
                if j in self.nonempty:
                    x = self.ider.idx(i)
                    y = self.ider.idx(j)
                    tot += table[i][j]
                    S[x][y] = table[i][j]
            for j in table[i]:
                if j in self.nonempty:
                    x = self.ider.idx(i)
                    y = self.ider.idx(j)
                    S[x][y] /= tot
        # Constructing A
        S = S.transpose()
        A = alpha*S+(1-alpha)/self.site_number*np.array([[1 for i in range(self.site_number)] for i in range(self.site_number)])
        ans = dict()
        # Iterating Pnow
        Pnow = np.array([[0 for i in range(self.site_number)]]).transpose()
        Plst = np.array([[0 for i in range(self.site_number)]]).transpose()
        Pnow[self.ider.idx(self.url)][0] = 1
        while np.linalg.norm(Pnow-Plst) >= eps:
            Plst = Pnow
            Pnow = np.matmul(A, Plst)
        ans = Pnow.transpose()[0]
        # Counstructing Answer
        pr = dict()
        for i in range(self.site_number):
            pr[self.ider.nam(i)] = ans[i]
        # pr = [(self.ider.nam(i), ans[i]) for i in range(self.site_number)]
        # pr = sorted(pr, key = lambda x: (self.webs.type[x[0]], x[1]), reverse = True)
        keys = list(self.webs.links)
        for i in keys:
            if not i in self.nonempty:
                self.webs.links.pop(i)
                self.webs.type.pop(i)
                self.webs.article.pop(i)
        self.pr = pr
        return pr

class SearchEngine:
    def __init__(self):
        self.webs = Webs()
        self.page_rank = dict()
        self.keyword_corlt = dict()
        self.weight = [0.1, 0.9]
        self.final_rank = dict()
        self.keyword = ""
        self.keywords = dict()
        self.rank = []
    def from_spider(self, sp):
        self.webs = sp.webs
        self.page_rank = sp.pr
        keywords = dict()
        for i in self.webs.article:
            keywords[i] = list(cut_for_search(self.webs.article[i].content, HMM = False))
        self.keywords = keywords
        return self
    def search(self, keyword = "中国"):
        self.keyword = keyword
        keywords = self.keywords
        self.rank = []
        tot = 0.
        for i in self.webs.article:
            cnt = 0
            for j in keywords[i]:
                if j == keyword:
                    cnt += 1
            self.keyword_corlt[i] = cnt/len(keywords)
            tot += cnt/len(keywords)
        # print(keywords["https://news.sina.com.cn/"])
        for i in self.webs.article:
            try:
                self.keyword_corlt[i] /= tot
            except:
                self.keyword_corlt[i] = 1/len(keywords)
        for i in self.webs.article:
            self.final_rank[i] = self.page_rank[i]*self.weight[0]+self.keyword_corlt[i]*self.weight[1]
            self.rank.append((i, self.final_rank[i]))
        self.rank = sorted(self.rank, key = lambda x: x[1], reverse = True)
        return self
    def top(self, N = 5):
        return self.rank[:min(N, len(self.rank))]

if __name__ == '__main__':
    sp = Spider()
    url = "https://news.sina.com.cn/"
    sp.get_sites(url, 2)
    lst = sp.page_rank(0.25)
    K = 10
    # for i in range(K):
    #     print("url =", lst[i][0], " pagerank =", lst[i][1])
    #     print(sp.webs.article[lst[i][0]].title)
    #     print(sp.webs.type[lst[i][0]])
    #     print(sp.webs.article[lst[i][0]].content)
    se = SearchEngine()
    se.from_spider(sp).search("特朗普")
    tops = se.top()
    for i in tops:
        print(f"url = {i[0]}, rank = {i[1]}")
        print(f"title = {sp.webs.article[i[0]].title}")