n1,n2=map(int,input().split())
if n1>n2:
    small=n1
else:
    small=n2
while(1):
    if ((small%n1)==0) and ((small%n2)==0):
        print(small)
        break
    small=small+1