k=int(input())
l=[]
for i in input().split():
    l.append(int(i))
l.sort()
print(l[0],end=' ')
print(l[-1],end='')    