k=int(input())
sum1=0
for i in range(2,k//2):
    if k%i==0:
        sum1=sum1+1
if(sum1>0):
    print("no")
else:
    print("yes")