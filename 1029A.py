av = input().split()
for i in range(len(av)):
	av[i] = int(av[i])

N = len(av)

ans = -1
for i in range(N):
	for j in range(i, N):
		ans = max(ans, min(av[i], av[j])*(j-i))

print(ans)

