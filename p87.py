def gcd(x,y):
    while(y):
        x,y=y,x%y
    return x 
n1,n2=map(int,input().split()) 
print(gcd(n1,n2))  