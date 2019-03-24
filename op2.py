n=input()
if n.isnumeric():
    if int(n)>0:
        if int(n)%2==0:
            print("Even")
        else:
            print("Odd")
    else:
        print("invalid")
else:
    print("invalid")