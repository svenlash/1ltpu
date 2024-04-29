def f(n):
    if n>=3000: return n
    if n<3000: return n+x+f(n+2)
x=-100
while f(2984)-f(2988)!=5916:
    x+=1
print(x)
    
    