import re
k=input()
if re.findall("[a-zA-z2-9]",k):
    print("no")
else:
    print("yes")    