n=int(input())
l=input().split()

k=[]
for i in range(n):
    if int(l[i])==i:
        k.append(i)
k=sorted(k)
if len(k)>0:
    for i in range(len(k)-1):
        print(k[i],end=' ')
    print(k[len(k)-1],end='')
else:
    print(-1)    
        
