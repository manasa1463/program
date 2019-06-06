n1,n2=map(int,input().split())
tot=0
for i in range(n1,n2+1):
    count=0
    for j in range(1,i+1):
        if(i%j==0):
            count=count+1
    if(count==2):
        tot=tot+1
print(tot)