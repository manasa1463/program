str1=input()
if (len(str1)%2==0):
    k=len(str1)//2
    print(str1[:k-1]+'*'+'*'+str1[k+1:])
else:
    k=len(str1)//2
    print(str1[:k]+'*'+str1[k+1:])