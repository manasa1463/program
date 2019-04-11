l=[i for i in input().split()]
k=''.join(l)
k=list(k)
d={}
for i in k:
    z=k.count(i)
    d[i]=z
max1=0
for i,j in d.items():
    if j>=max1:
        max1=j
        t=i
print(t)    