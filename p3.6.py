n=int(input())
k=input().split()
flag=False
for i in k:
    if k.count(i)>1:
        print(i,end='')
        flag=True
        break
if flag==False:
    print(-1)       