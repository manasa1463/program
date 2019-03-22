n=input()
n1=int(n)
l=[i for i in map(int,input().split())]
l.sort()
k=l[n1//2]
print(k)