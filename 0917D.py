av = input()
av = av.split()
n = len(av)
for i in range(n) :
	av[i] = int(av[i])

maxn = max(av)
out = ''
for i in range(n) :
	if(av[i] == maxn) :
		out += str(i+1)+' '

print(out)
