n,m=input().split()
a=input().split()
b=input().split()
a=''.join(sorted(a))
b=''.join(sorted(b))
if b in a:
    print("Yes")
else:
    print("No")    

