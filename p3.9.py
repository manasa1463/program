l=list(map(int,input().split()))
sum1=l[0]+l[1]
lwr=0
upr=1
for i in range(len(l)-1):
    for j in range(i+1,len(l)):
        sum2=l[i]+l[j]
        if abs(sum1)>abs(sum2):
            sum1=sum2
            lwr=i
            upr=j
print(l[lwr],l[upr])            
     