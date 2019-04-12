s1,s2,k=input().split()
k=int(k)
l1=[i for i in s1]
l1=list(set(l1))
l2=[i for i in s2]
l2=list(set(l2))
sum1=0
if len(l1)==len(l2):
    sum1=0
    for i in range(len(l1)):
        if l1[i] in l2:
              pass
        else :
            sum1=sum1+1
if sum1==k:
    print("yes")
else:
    print("no")            