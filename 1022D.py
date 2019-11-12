import re
s = input()
#print(s)
dividend = re.search("dividend\s*=\s*-?[0-9]+", s)
divisor = re.search("divisor\s*=\s*-?[0-9]+", s)
#print(dividend)
#print(divisor)
if dividend == None or divisor == None:
	print("No")
else:
	dividend = int(re.search("-?[0-9]+", dividend.group(0)).group(0))
	divisor = int(re.search("-?[0-9]+", divisor.group(0)).group(0))
	try:
		print(dividend//divisor)
	except:
		print("No")
