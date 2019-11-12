s = input()

s = s.lower()
s = s.split()
n = len(s)

for i in range(n) :
	s[i] = s[i].capitalize()

if(n > 2) :
	for i in range(1, n-1):
		s[i] = s[i][0]+'.'

s = " ".join(s)

print(s)
