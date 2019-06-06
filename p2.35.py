n=input()
k=''.join(n.lower().split())
l=[]
for i in k:
    if k.count(i)==1:
        l.append(i)
for i in range(len(l)):
    print(l[i],end=' ')
