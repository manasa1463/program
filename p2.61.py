n,k=map(int,input().split())
l=list(map(int,input().split()))
l1=[ (i,j) for i in range(len(l)) for j in range(i+1,len(l)) if l[i]+l[j]==k]
if len(l1)>0:
    print("yes")
else:
    print("no")    
