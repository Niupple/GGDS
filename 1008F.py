ori = []
usd = dict()
av = dict()
N = int(input())

for i in range(N):
	a = input().split()
	ori.append(a)
	for s in a:
		s = s.lower()
		av[s] = av.get(s, 0)+1

bv = []
for i in av:
	bv.append((i, av[i]))

bv = sorted(bv, key = lambda key: key[-1], reverse = True)
maxn = bv[0][-1]
print(maxn)
for i in ori:
	for j in i:
		j = j.lower()
		if av[j] == maxn and usd.get(j, True):
			print(j)
			usd[j] = False

