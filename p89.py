str1=input()
l=[]
for i in range(0,len(str1)):
    l.append(ord(str1[i]))
l.sort()
for i in l:
    print(chr(i),end='')