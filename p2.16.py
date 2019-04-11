n=int(input())
l=[i for i in input().split()]
d={}
for i in l:
    z=l.count(i)
    d[i]=z
print(d)    
for i,j in d.items():
    if j==1:
        print(i)