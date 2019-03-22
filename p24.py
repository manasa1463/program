n=input()
n1=int(n)
l=[i for i in map(int,input().split())]
l.sort()
for i in range((n1-1)):
    print(l[i],end=' ')
else:
   print(l[-1],end='')   