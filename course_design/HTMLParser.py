import sys
import pickle
import numpy as np
from re import search
from re import findall
from urllib.parse import urljoin
from urllib.parse import urlparse
from urllib.request import Request
from urllib.request import urlopen
from html.parser import HTMLParser
from queue import Queue

url = "https://news.sina.com.cn/c/xl/2018-12-31/doc-ihqfskcn2945759.shtml"

class iParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.links = []
    def clear_links(self):
        self.links = []
    def handle_starttag(self, tag, attrs):
        if(tag == 'a' and attrs[0][0] == 'href' and attrs[0][1] != '#'):
            self.links.append(attrs[0][1])
        # if(tag == 'p'):
        #     print("tag =", tag)
        #     print("attrs =", attrs)
    # def handle_data(self, data):
    #     print("data = ", data)

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
                print(j)
                lines[i] = lines[i].replace(j, "")
                # print(lines[i])
            print(lines[i])
        self.content = "\n".join(lines)
        return self
        
Parser = iParser()
r = Request(url, headers={'User-agent': 'Mozilla 5.10'})
t = urlopen(r, timeout = 10)
Parser.clear_links()
txt = t.read().decode("utf-8")
# print(txt)
# a = findall(r"(?<=<p>)[^<>]*(?=</p>)", txt)
# a = "\n".join(a)
# # print(a.groups[0])
# Parser.feed(txt)
a = Artical().from_html(txt)
print(a.content)