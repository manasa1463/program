n1,n2=map(int,input().split())
sum1=0
li=[]
for i in range(1,n2+1):
    o=i
    g=o**2
    li.append(g)
for i in range(n1,n2+1):
    if i in li:
        sum1=sum1+1
print(sum1)       