s1,s2=input().split()
if len(s1)!=len(s2):
    print("no")
else:    
    tot=0    
    for i in range (len(s1)):
        if (s1[i]!=s2[i]):
            tot=tot+1
    if tot==1:
        print("yes")
    else:
        print("no")