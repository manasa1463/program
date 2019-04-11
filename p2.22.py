def gcd(x,y):
    while(y):
        x,y=y,x%y
    return x 
n2,n3=map(int,input().split()) 
print(gcd(n2,n3))