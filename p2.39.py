n=int(input())
k=True
while (k):
    if n==1:
        k=True
        break
    if n%2==0:
        n=n//2
        k=True
    else:
        k=False
if k==False:
    print("no")
else:
    print("yes")    