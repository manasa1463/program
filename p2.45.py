p,a=map(int,input().split())
k=[(i,j) for i in range(p) for j in range(p) if i+j==(p/2) and i*j==a]
if len(k)>0:
    print("yes",end='')
else:
    print("no",end='')    