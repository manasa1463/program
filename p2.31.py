str1=input()
l=[]
for i in range(len(str1)):
    l.append(str1[i])
c=l.count('(')
c1=l.count(')')
if c==c1:
    print("yes")
else:
    print("no")    
