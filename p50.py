n=int(input())
k=round(pow(n,0.5))
l=[]
for i in range(0,k):
    t=pow(2,i)
    l.append(t)
if n in l:
    print("yes")
else:
    print("no")    