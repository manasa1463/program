n=int(input())
l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
l3=[]
for i in l1:
    if i in l2:
        l3.append(i)
for i in range(len(l3)-1):
    print(l3[i],end=' ')
print(l3[len(l3)-1],end='')        