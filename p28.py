n=input()
n1=int(n)
l=[i for i in map(int,input().split())]
for k in range(n1):
    if(k!=n1-1):
        print("{} {}\n".format(l[k],k))
    else:
        print("{} {}\n".format(l[k],k))