import math
n=int(input())
n=math.radians(n)
if (n>0 and n<1):
    print(round(math.sin(n),2),end='')
else:
    print(round(math.sin(n)),end='')    