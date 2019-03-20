x,y,z = input().split(" ")
x = int(x)
y = int(y)
z=  int(z)

if((x>y)&(x>z)):
    print(x)
elif((y>x)&(y>z)):
    print(y)
else:
    print(z)