n,k=map(int,input().split())
l=[int(i) for i in input().split()]
try:
    for i in l[-k:]:
        print(i,end=' ')
        for i in l[:-k-1]:
            print(i,end=' ')
            print(l[-k-1],end='')    
except IndexError:
    for i in range((len(l)-1)):
        print(l[i],end=' ')
    print(l[(len(l)-1)],end='')   