from functools import cache 
@cache 
def f(n):
    if n==0: return 1 
    if n>0: return 2*f(1-n)+3*f(n-1)+2
    if n<0: return -f(-n)
a=f(50)
b=0
for i in str(a):
    b+=int(i)
print(b)
