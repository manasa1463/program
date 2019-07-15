s1,s2=input().split()
Flag=False
if len(s1)==len(s2):
    for i in range(len(s1)):
        if s1[i]==s2[i]:
            flag=True
        else:
            flag=False
            break
if flag==True:
    print("yes",end='')
else:
    print("no",end='')        