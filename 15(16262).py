def f(a,x,y):
    return ((a<x)or(x**2-7*x+10>0))and((a>=y)or(y**2+7*y+12>0))
k=0
for a in range(-200,200):
    if all(f(a,x,y) for x in range (-200,200) for y in range (-200,200)):
        k+=1
        print(k)
#5