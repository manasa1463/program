n1,n2=map(int,input().split())
if n1>n2:
    min1=n1
else:
    min1=n2
while(1):
    if ((min1%n1)==0) and ((min1%n2)==0):
        print(min1)
        break
    min1=min1+1