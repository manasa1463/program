n=int(input())
n1=n
temp=0
k=0
while(n>0):
    k=n%10
    temp=temp*10+k
    n=n//10
if(temp==n1):
	print("yes")
else:
	print("no")