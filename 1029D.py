val = { 1: "I", 
		5: "V", 
		10: "X", 
		50: "L", 
		100: "C", 
		500: "D", 
		1000:"M" }

N = int(input())
x = N
ans = ""
for i in range(4, -1, -1):
	#print(i)
	b = 10**i
	c = x//b
	x %= b
	if c == 0:
		continue
	elif c == 9:
		ans += val[b]+val[10*b]
		continue
	elif c >= 5:
		ans += val[5*b]
		c -= 5
	
	if c == 4:
		ans += val[b]+val[5*b]
	else:
		ans += c*val[b]
print(ans)

