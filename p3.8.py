n=int(input())
l=list(map(int,input().split()))
for i in range(n):
    for j in range(n):
        for k in range(n):
            if i<j<k:
                if l[i]+l[j]==l[k]:
                    print(l[i],l[j],l[k])
              