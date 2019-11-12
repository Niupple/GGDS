def lcp(a, b):
	l = min(len(a), len(b))
	ret = ""
	for i in range(l):
		if a[i] == b[i]:
			ret += a[i];
		else:
			return ret
	return ret
N = int(input())
ans = None
for i in range(N):
	s = input()
	if ans == None:
		ans = s;
	elif ans == "":
		break;
	else:
		ans = lcp(ans, s)

if ans == "":
	print("No")
else:
	print(ans)
