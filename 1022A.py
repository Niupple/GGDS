import re
s = input()

ans = re.match("114514-g[-\w]* s[-\w]* t[-\w]*( [-\w])*$", s)
if not ans == None:
	print("Yes")
else:
	print("No")
