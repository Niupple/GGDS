N = 17
table = [7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
varif = ['1','0','X','9','8','7','6','5','4','3','2']

def check(x) :
	if len(x) != 18:
		#print("length no 18")
		return False
	sm = 0
	for i in range(0, N):
		if not x[i].isdigit() :
			#print("non digit in prev 17 cha")
			return False
		sm += int(x[i])*table[i]
	sm %= 11
	if varif[sm] == x[N]:
		return True
	else:
		#print("varify error")
		return False
	return False

line = input()
lst = []

for i in line:
	lst.append(i)

if check(line):
	print("YES")
else:
	print("NO")
