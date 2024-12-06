import sys
sys.setrecursionlimit(20000) 
def f(x,y):
    if x>y or x==33:
        return 0
    if x==15:
        return 1
    if x==y:
        return 1
    return f(x+1, y) + f(x*2, y) + f(x*3, y)
print(f(3, 50)) 
