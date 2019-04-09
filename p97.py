n=int(input())
sum1=0
while(n):
    k=n%10
    sum1=sum1*10+k
    n=n//10
print(sum1)    