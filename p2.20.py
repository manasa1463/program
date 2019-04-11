s=input()
for i in range(len(s)):
    if (((ord('z')-ord(s[i]))>=3) and ((ord('z')-ord(s[i]))<=26)) or (((ord('Z')-ord(s[i]))>=3) and ((ord('Z')-ord(s[i]))>=3)):
        print(chr(ord(s[i])+3),end='')
    elif (ord('z')-ord(s[i]))<3:
        k=(ord(s[i])-ord('z'))+97+2
        print(chr(k),end='')
    else:
        k=(ord(s[i])-ord('Z'))+65+2
        print(chr(k),end='')
