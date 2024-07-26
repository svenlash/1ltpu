for a in range(-100,100):
    flag=True
    for x in range(-100,100):
        for y in range(-100,100):
            if (((x+y)<=30)or(y<=(x+2))or(y>=a))==0:
                flag=False
                break
    if flag: print(a) 
'''17'''
