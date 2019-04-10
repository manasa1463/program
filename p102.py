import math
def div(n1):
    if n1%2==0:
        return div(n1/2)
    else:
        return math.ceil(n1)
n=int(input())    
print(div(n))    
    