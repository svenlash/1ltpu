for a in range(1, 100000000000):
    flag=True
    for x in range(1, 500):
        if ((x%a != 0) <= ((x%28 == 0) <= (x%49 != 0))) == 0:
            flag=False
            break
    if flag: print(a)
"""196"""
