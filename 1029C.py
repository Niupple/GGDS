val = { "I" : 1, 
		"V" : 5, 
		"X" : 10, 
		"L" : 50, 
		"C" : 100, 
		"D" : 500, 
		"M" : 1000 }
av = input()
bv = []
s = ""
N = len(av)

for i in range(N):
	s += av[i]
	if (i+1 < N and val[av[i]] >= val[av[i+1]] and s != "") or i+1 == N:
		bv.append(s)
		s = ""

ans = 0
for i in bv:
	if len(i) == 1:
		ans += val[i]
	else:
		ans += val[i[-1]]-val[i[0]]

print(ans)

