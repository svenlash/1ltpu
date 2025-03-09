'''def f(x, y):
    if x>=132: return y%2==0
    if y==0: return 0
    h = [f(x+3, y-1), f(x+6, y-1), f(x*3, y-1)]
    return any(h) if y%2==1 else all(h)
print([i for i in range(1,132) if f(i,2)])
print(sorted([i for i in range(1,132) if f(i, 3) and not f(i, 1)]))
print(min([i for i in range(1,132) if f(i,2) or f(i, 4)]))

def f(x,y,z):
    if x+y>=65: return z%2==0
    if z==0: return 0
    h=[f(x+1,y,z-1),f(x,y+1,z-1),f(x*3,y,z-1),f(x,y*3,z-1)]
    return any(h) if y%2==1 else all(h)
print([s for s in range(1,59) if f(6, s, 2) or f(6,s,4)] )
'''
def f(a, b, m):
    if a+b >=65:return m%2==0
    if m==0: return 0
    h =[f(a+1, b, m-1), f(a, b+1, m-1),
        f(a*3, b, m-1), f(a, b*3, m-1)]
    return any(h) if m%2==1 else all(h)
print(([s for s in range(1,59) if f(6,s,2)]))
print([s for s in range(1,59) if f(6,s,3) and not f(6, s, 1)])
print([s for s in range(1,59) if f(6,s,4) and not f(6, s, 2)])