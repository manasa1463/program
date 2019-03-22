n=input()
k=len(n)
n1=int(n)
l=n1
sum=0
temp=0

for i in range(k):
    temp=n1%10
    sum=sum+temp**k
    n1=n1//10

if(l==sum):
   print("yes")
else:
    print("no")