line = input()
out = []
stk = []
cnt = 0
flag = True
for i in range(len(line)):
	if not flag:
		break
	if line[i] == 'A':
		cnt += 1
		out += str(cnt)
	elif line[i] == 'B':
		if len(stk) < 5:
			cnt += 1
			stk.append(cnt)
		else:
			flag = False;
			break
	else:
		if len(stk) > 0:
			out += str(stk[-1])
			stk.pop()
		else:
			flag = False
			break

if flag:
	print("Yes")
	for i in out:
		print(i)
else:
	print("No")

