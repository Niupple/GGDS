maps = dict()
N = int(input())
order = dict()
cnt = 0;

def get_id(x):
	global cnt
	if order.get(x, -1) == -1:
		order[x] = cnt
		cnt += 1
	return order[x]

for i in range(N):
	s = input()
	f = get_id(s[0])
	for j in range(1, len(s)):
		if s[j].isalpha():
			t = get_id(s[j])
			v = ""
			for k in range(j+2, len(s)):
				if s[k].isdigit():
					v += s[k]
				else:
					break
			v = int(v)
			maps[(f, t)] = v

for i in range(cnt):
	for j in range(cnt):
		print(maps.get((i, j), 0), end = " ")
	print()

