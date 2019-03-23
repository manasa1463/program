count1=0
l=input()
count=len(l)
for i in l:
    if (i.isalpha()) or (i.isspace()) or (i.isnumeric()):
        count1=count1+1
count=count-count1
print(count)
