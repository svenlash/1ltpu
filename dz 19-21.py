'''#1
def f(a,b,x):
    if a+b>=65: return x%2==0
    if x==0: return 0
    h = [f(a+1, b, x-1), f(a, b+1, x-1), f(a*3, b, x-1), f(a, b*3, x-1)]
    return any(h) if x%2==1 else all(h)
print([o for o in range(1,59) if f(6,o,2)]) #7
print([o for o in range(1,59) if f(6,o,3) and not f(6,o, 1)]) #10 19
print([o for o in range(1,59) if f(6, o,4) and not f(6,0,2)]) #18
'''

'''def f(a,x):
    if a>=342: return x%2==0
    if x==0: return 0
    h =[f(a+7,x-1),f(a*3,x-1)]

    return any(h) if x%2==1 else all(h)
print([i for i in range(1,301) if f(i,2)]) #113
print([i for i in range(1,301) if f(i,3) and not f(i,1)])#36 37 '''

'''def f(a,b,m):
    if a+b>=150: return m%2==0
    if m==0: return 0
    h = [f(a+2,b,m-1),f(a,b+2,m-1),f(a*3,b,m-1),f(a,b*3,m-1)]
    return any(h) if m%2==1 else all(h)
print([i for i in range(1,134) if f(16,i,4) and not f(16,i,2)]) #43
'''

'''def f(a,x):
    if a>33: return x%2==0
    if x==0: return 0
    h = [f(a+1,x-1),f(a+2,x-1),f(a+3,x-1),f(a*2,x-1)]
    return any(h) if x%2==1 else all(h)
print([p for p in range(1,34) if f(p,2)]) #16'''

def f(a,b,x):
    if a*b>=123: return x%2==0
    if x==0: return 0
    h = [f(a+2,b,x-1), f(a*2,b,x-1), f(a,b+2,x-1), f(a,b*2,x-1)]
    return any(h) if x%2==1 else all(h)
#print([k for k in range(1,225) if f(15,k,3) and not f(15,k,1)]) #107 114
print([s for s in range(1,41) if f(3,s,4) and not f(3,s,2)]) #16