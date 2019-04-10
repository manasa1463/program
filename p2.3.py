n=int(input())
rev=0
k=0
while(n):
    k=n%10
    rev=rev*10+k
    n=n//10
print(rev)    
