def binary(li,l,u,k):
    if u>=l:
        mid=((l+u)//2)
        if li[mid]==k:
            return True
        if k<li[mid]:
            return binary(li,l,mid-1,k)
        else:
            return binary(li,mid+1,u,k)

n,k1=map(int,input().split())
l1=[int(i) for i in input().split()] 
u1=(len(l1)-1)
r1=binary(l1,0,u1,k1)
if(r1==True):
    print("yes")
else:
    print("no")    