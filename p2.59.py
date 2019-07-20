import re
n=int(input())
st=input()
count=0
for m in re.finditer('0',st):
    count=m.start() 
l=[]
for i in range(count):
    if st[i]=='1':
        l.append(int(st[i]))
for i in range(len(l)-1):
    print(l[i],end=' ')
print(l[len(l)-1],end='')  
