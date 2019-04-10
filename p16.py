n1,n2=map(int,input().split())
l=[]
for i in range(n1+1,n2):
    sum1=0
    for i1 in range(2,((i//2)+1)):
        if i%i1==0:
            sum1=sum1+1
    if sum1==0:
        l.append(i)
k=len(l)
for digit in range(k-1):
    print(l[digit],end=' ')
print(l[k-1],end='')    