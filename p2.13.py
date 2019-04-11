n=int(input())
k=0
sum1=0
while(n):
    k=n%10
    sum1=sum1+k**2
    n=n//10
print(sum1)    