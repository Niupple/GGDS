n = int(input())
k = int(input())
av = {}
for i in range(n):
	x = int(input())
	if(av.get(x, 0) < k):
		av[x] = av.get(x, 0)+1
		print(x)
