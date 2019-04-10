n1,n2=map(int,input().split())
for i in range(n1+1,n2):
    rev=i
    k=0
    sum1=0
    rev1=i
    digit=0
    while(rev1):
        rev1=rev1//10
        digit=digit+1
    while(i):
        k=i%10
        sum1=sum1+k**digit
        i=i//10
    if(rev==sum1):
        print(rev)
        