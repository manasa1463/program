n=list(map(str,input().split()))
l1=[]
for i in n:
    l1.append(i[::-1])
for i in range(len(l1)-1):
    print(l1[i],end=' ')
print(l1[len(l1)-1],end='')    