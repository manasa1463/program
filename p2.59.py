import re
n=int(input())
k=list(map(str,input().split()))
st=''.join(k)
count=0
for m in re.finditer('0',st):
    count=m.start() 
l=[]
for i in range(count):
    if k[i]=='1':
        l.append(int(k[i]))
print(l)
for i in range(len(l)-1):
    print(l[i],end=' ')
print(l[len(l)-1],end='')  
