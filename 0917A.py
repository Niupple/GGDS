n = int(input())
i = 2;
if n == 1:
	print("N")
	quit()
elif n == 0:
	print("N")
	quit()
while i*i <= n:
	if n%i == 0:
		print("N")
		quit()
	i = i+1

print("Y")
