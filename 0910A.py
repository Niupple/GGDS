lst = []
while True:
	tmp = input()
	if tmp == '':
		break
	else:
		lst.append(int(tmp))

n = len(lst)+1
m = lst[n//2-1]
lst.sort()
lst.reverse()

print(lst[0])
print(lst[-1])
print(m)

for i in range(0, n-1):
	lst[i] = str(lst[i])

out = ' '.join(lst)

print(out)
