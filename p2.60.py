s1,s2=input().split()
flag=False
for i in s1:
    if i in s2:
        flag=True
        break
if flag==True:
    print("yes",end='')
else:
    print("no",end='')    