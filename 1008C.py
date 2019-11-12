tmp = ""
ans = []
av = input()
for i in av:
	if i.isupper():
		if tmp != "":
			ans.append(tmp)
		tmp = ""
	tmp += i.lower()

if tmp != "":
	ans.append(tmp)

print(*ans, sep='_')
