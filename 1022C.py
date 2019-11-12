av = input().split()
bv = input().split()

N = len(av)
for i in range(N):
	if bv[i] == "B-LOC":
		print("<LOC>", end = "")
	print(av[i], end = "")
	if (bv[i] != "O" and (i == N-1 or bv[i+1] != "I-LOC")):
		print("</LOC>", end = "")
print()
