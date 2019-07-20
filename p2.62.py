import math
n=int(input())
for i in range(1,n+1):
    k=n/i
    if k%2!=0:
        if k is not 0 and math.floor((k%2))==math.ceil((k%2)):
            print(i)
            break;
