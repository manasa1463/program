import re
str1=input()
k=re.findall('[0-9]',str1)
for  i in k:
    print(i,end='')