try:
    k=int(input())
    if(k>=-2**15+1 and k<=2**15+1):
        print("INT",end='')
    elif(k>=-2**31+1 and k<=-2**31+1):
        print("LONG",end='')
    else:
        print("LONG LONG")
except:
    print("invalid",end='')        