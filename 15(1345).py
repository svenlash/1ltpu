def g(x,a,Q):
    return ((x%3!=0) and x!={48, 52, 56}) <= (((abs(x-50)<=7)<=(x==Q) or (x&a==0)))
for a in range(1,100):
    if all(g(x,a,Q) for x in range(1,100) for Q in range (29,50)):
        print(a)
        