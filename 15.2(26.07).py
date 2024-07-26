for a in range(1,5000):
    flag=True
    for x in range(1,5000):
        if (((x%12==0)<=(x%42!=0))or((x+a)>=4096))==0:
            flag=False
            break
    if flag: print(a)
'''4012'''
