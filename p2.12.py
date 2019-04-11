n,k=map(int,input().split())
l1=[]
l=[int(i) for i in input().split()]
if k>n:
    k=k%n
for i in l[-k:]:
    l1.append(i)
for i in l[:-k]:
    l1.append(i)
for i in range((len(l1)-1)):
    print(l1[i],end=' ')
print(l1[(len(l1)-1)],end='')    
