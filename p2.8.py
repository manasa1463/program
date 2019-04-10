l=[i for i in input().split()]
k=len(l)
for i in range(k-1):
    print(l[i].capitalize(),end=' ')
print(l[k-1].capitalize(),end='')    