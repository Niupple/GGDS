N = int(input())
av = []

for i in range(N):
	a = input()
	b = input()
	av.append((a,float(b)))

out = sorted(av, key = lambda x: x[-1], reverse=True)
for i in out:
	print ("%s, %.2f" % i)

