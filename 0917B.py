n = 0
av = [0, 0]
flag = True

while (flag):
	x = int(input())
	if(x == -1) :
		break
	av[x] += 1
	n += 1

if(av[1] >= av[0]) :
	print("Yes")
else:
	print("No")
