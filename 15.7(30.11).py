def H(x,a):
    return (x%a!=0) <= ((x%14==0)<=(x%4!=0))
for a in range(1,1000):
    if all(H(x,a) for x in range (1,1000)):
        print(a)
#28