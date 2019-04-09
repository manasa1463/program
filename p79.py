import math
n,m=map(int,input().split())
l=math.sqrt(n*m)
if (l-int(l)==0.0):
    print("yes")
else:
    print("no")    