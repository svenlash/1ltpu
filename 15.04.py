def f(x):
    i=0
    for a in str(x):
        if int(a)<i:
            return False
        i=int(a)
    return True 
c=0
for x in range(1395,22717+1):
    if f(x):
        c+=x
print(c)