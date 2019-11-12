n = int(input())

for i in range(n):
	out = ''
	for j in range(n):
		if(i == j):
			out += "1 "
		else:
			out += "0 "

	print(out)
