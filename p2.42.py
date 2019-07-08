n=int(input())
l=list(map(int,input().split()))
if (l==sorted(l)):
    print("yes",end='')
else:
    print("no",end='')    
