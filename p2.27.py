s=input()
for i in s:
    if(i.islower()):
        k=ord(i)-32
        print(chr(k),end='')
    if(i.isupper()):
        k=ord(i)+32
        print(chr(k),end='')