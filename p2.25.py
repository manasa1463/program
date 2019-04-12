n=int(input())
l=[i for i in input().split()]
for j in range(len(l)):
    for i in range((len(l)-j-1)):
        if(len(l[i])>len(l[i+1])):
            l[i],l[i+1]=l[i+1],l[i] 
        if (len(l[i])==len(l[i+1])):
                for j in range(len(l[i])):
                    if l[i][j]>l[i+1][j]:
                        print(l[i][j],l[i+1][j])
                        l[i],l[i+1]=l[i+1],l[i]
                        break
                    elif l[i][j]<=l[i+1][j]:
                        break
                    else:
                        pass
for k in range((len(l)-1)):
    print(l[k],end=' ')
print(l[(len(l)-1)],end='')
    
    
