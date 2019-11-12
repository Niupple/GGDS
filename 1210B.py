N = int(input())
av = sorted(list(set(map(int, input().split()))))
maxdiff = 0;
L = len(av)
for i in range(L-1):
	maxdiff = max(av[i+1]-av[i], maxdiff)

for i in range(L-1):
	if(av[i+1]-av[i] == maxdiff):
		print(av[i], av[i+1])
