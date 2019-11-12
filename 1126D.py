cnt = 0
idx = dict()
node = dict()

def get_id(x):
	global cnt
	if not x in idx:
		idx[x] = cnt
		cnt += 1
	return idx[x]

def add_edge(f, t):
	if not f in node:
		node[f] = [t]
	else:
		node[f].append(t)

N, end = input().split()
N = int(N)
end = (end)

for i in range(N):
	line = input()
	ns = line[line.index("{")+1:line.index("}")].strip()
	f = (line[0])
	ns = ns.split(",")
	for j in ns:
		j = j.strip().split(":")
		t = (j[0])
		add_edge(f, t)

instk = set()
usd = set()
def dfs(x):
	flag = False
	if x == end:
		return True
	for now in node[x]:
		if now in instk:
			return False
		else:
			instk.add(now)
			ret = dfs(now)
			instk.remove(now)
			if(ret):
				flag = True
			else:
				return False
	return flag

ans = []
usd.add(end)
for i in node:
	if not i in usd:
		if dfs(i):
			ans.append(i)
		usd.add(i)

if len(ans) == 0:
	print("None")
else:
	print(" ".join(sorted(ans)))

