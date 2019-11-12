from __future__ import print_function
l=[]
l1=[]
l2=[]
while True:
    c=input()
    if c=='':
        break
    c=int(c)
    l.append(c)
    if c>0:
        l1.append(c)
    else:
        l2.append(c)
l1=sorted(l1)
l2=sorted(l2)
k=(len(l)+1)//2-1
print(l1[-1],l2[0],l[k])
l=l2+l1
l=reversed(l)
for name in l:
    print (name,end=' ')

