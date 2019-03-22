n,a,d=input().split(' ')
n1=int(n)
a1=int(a)
d1=int(d)
if (1<=n1<=100000)and(1<=a1<=100000)and(1<=d1<=100000):
    k=((n1/2)*(2*a1+(n1-1)*d1))
    print(int(k))