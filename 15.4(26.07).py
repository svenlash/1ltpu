for a in range(1,10000000):
    flag=True
    b=[x for x in range(70, 91)]
    for x in range(1,10000):
        if ((x%a==0)or((x in b)<=(x%22!=0)))==0:
            flag=False
            break
    if flag: print(a)
'''88'''
