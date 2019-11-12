n = int(input())
av = {}
for i in range(n):
	s = input().split()
	a = s[0]
	b = int(s[1])
	av[a] = av.get(a, 0)+b

n = int(input())
for i in range(n):
	s = input().split()
	a = s[0]
	b = int(s[1])
	av[a] = av.get(a, 0)+b

x = input()
print(av[x])
