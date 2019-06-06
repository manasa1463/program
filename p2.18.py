n=int(input())
count=0
l=[]
for i in range(n):
    l.append(input())
for i in range(n):
    if sorted(l[i])==sorted('kabali'):
        count=count+1
print(count)        