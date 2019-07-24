n,k=map(int,input().split())
l=list(map(int,input().split()))
k1=sorted(l,reverse=True)
print(k1[k-1])