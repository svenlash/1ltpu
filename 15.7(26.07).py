for a in range(1,1000):
    flag=True
    for x in range(1,1000):
        if (((x&a)!=0)<=(((x&168)==0)<=((x&69)!=0)))==0:
            flag=False
            break
    if flag: print(a)
'''237'''
