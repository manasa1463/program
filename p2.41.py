n,p=map(int,input().split())
i=1
flag=False
while(n>=(p**i)):
    if n==(p**i):
        flag=True
        break
    else:
        i=i+1
if flag==True:
   print("yes",end='')
else:
   print("no",end='')    
