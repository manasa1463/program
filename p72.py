import re
k=input()
if re.findall('[aeiou]',k):
    print('yes')
else:
    print('no')    