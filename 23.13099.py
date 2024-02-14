from itertools import product
def f(c,e,z):
    if c>e+100:
        return 0
    if c==e:
        return 1
    if z=='A':
        return f(c*2,e,'B')+f(c*3,e,'C') 
    if z!='A':
        return f(c-1,e,'A')+f(c*2,e,'B')+f(c*3,e,'C')
print(f(3,15,''))