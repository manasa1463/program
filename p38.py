x,y=input().split(' ')
x=int(x)
y=int(y)
x,y = (x^y)^((x^y)^y),(x^y)^y
print(x,end=' ')
print(y,end='')
