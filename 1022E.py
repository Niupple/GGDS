import re
s = input()

#print(s)
ans = re.match("^(([0-9]{5})|(([0-9]{8})|(((ZY)|(SY)|(BY))[0-9]{7})))$", s)
if ans == None:
	print("False")
else:
	print("True")

