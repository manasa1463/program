import re
n=int(input())
s=input()
k=re.sub('[aeiou]','',s)
print(k[::-1])