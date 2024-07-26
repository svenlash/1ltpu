for a in range(1,10000):
    flag=True
    for x in range(1,10000):
        if ((x%a==0)or((x%133==0)<=(x%95!=0))) == 0:
            flag=False
            break
    if flag: print(a)
'''665'''
