import re

line = input()

sent = line.split('.')
for i in range(0, len(sent)):
	sent[i] = sent[i].strip(' ')
	if(len(sent[i]) >= 1) :
		sent[i] = sent[i].lower()
		tmp = ''
		tmp += (sent[i][0].upper())
		for j in range(1, len(sent[i])):
			tmp += (sent[i][j])
		sent[i] = tmp

line = ''
for i in sent:
	if i != '':
		line += (i+". ")

#flag = True
line = re.sub(r'\bi\b', 'I', line)
'''
while True:
	ran = re.match('i', line)
	print('mama', ran)
	if ran == None:
		break
	else:
		ran = ran.span()
		for i in ran:
			line[i] = line[i].upper()
'''
print(line)
