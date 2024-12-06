def R(x,a):
    return (x&29 == 0) or ((x&11 == 0) <= (not(x&a == 0)))
for a in range(0,1000): 
    if all(R(x,a) for x in range(15,31)):
        print(a)
        break
#16