n = int(input())
av = []
for i in range(n):
	x = int(input())
	av.append(x)

bv = list(range(n))
maxn = -1
cnt = 0
for i in reversed(range(n)):
	if(av[i] < maxn):
		bv[i] = 0
	else:
		bv[i] = 1
		cnt += 1

	maxn = max(av[i], maxn)

print(cnt)
for i in range(n):
	if(bv[i] == 1):
		print(i+1)
