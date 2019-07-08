n,m=input().split()
m=int(m)
if m<=len(n):
    m=m%(len(n))
print(n[m::],end='')
print(n[0:m],end='')

    