s1,s2=map(str,input().split())

for (value,letter) in enumerate(s1):
    s1=s1.replace(letter,str(value))

for (value,letter) in enumerate(s2):
     s2=s2.replace(letter,str(value))

if s1==s2:
     print("yes")
else:
     print("no")     
    