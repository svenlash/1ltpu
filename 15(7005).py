def f(a,x):
    return (37+a+x+45==180) == ((a+x==90) and (a<=97))
for a in range(1,1000):
    if all(f(a,x) for x in range (1,1000)): print(a)
