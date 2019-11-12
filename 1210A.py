HASH_BASE = 100
def hash(k: int):
	global HASH_BASE
	return k % HASH_BASE

table = [set() for i in range(HASH_BASE)]
N = int(input())
av = list(map(int, input().split()))
bv = set(av)
L = len(bv)
tot = 0

def add(x):
	h = hash(x)
	table[h].add(x)

for i in bv:
	add(i)

for s in table:
	n = len(s)
	tot += n*(n+1)/2

print("%.2f" % (tot/L))

