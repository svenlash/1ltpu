def xor(a,b):
    return (a and not(b)) or (b or not (a))
def f(x,a):
    return (xor(x,a)!=2) and not ((xor(x,9)!=5)<=(xor(x,27)!=7))==0
for a in range(0,999):
    if all(f(x,a)for x in range(0,1000)):
        print(a)
        break