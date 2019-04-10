n=int(input())
prod=1
k=0
while(n):
    k=n%10
    prod=prod*k
    n=n//10
print(prod)
  