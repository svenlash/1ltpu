#14338

f={}
g={}
for n in range(8,2205):
    if n<10:
        f[n]=n
        g[n]=n
    else:
        f[n]=3*n + g[n-2]
        g[n]=n-2 + f[n-1]
print(f[2204] - g[2200])

#11819

f={}
g={}
for n in range(-1000,1112):
    if n<10:
        f[n]=n
        g[n]= -n
    else:
        f[n]=g[f[n-1]%10] + f[g[n%10]-1] - f[n-3]
        g[n]=f[g[n-1]%10] + g[f[n-1]-1] + g[n-2]
print(f[1111] + g[1111])

#9371
from functools import *
@lru_cache(None)
def f(n):
    if n>=3210: return 1
    else: return f(n+3)+7
@lru_cache(None)
def g(n):
    if n<10: return n
    else: return g(n-3)+5
for i in range(3210, 15, -1):
    f(i)
for i in range(10,3000):
    g(i)
print(f(15)-g(3000))


f={}
for n in range(-20,7000):
  if n<=1: f[n]=0
  if n>1 and n%6==0: f[n]=n+f[n/6-2]
  if n>1 and n%6==1: f[n]=n+f[n+6]
for i in range(-10, 4000): f[n]
print(f[202])

f = {}
g = {}
for n in range(-1000, 3001):
    if n < 10: g[n] = n #нерекусивный
    else: g[n] = g[n-3] + 5 #рекурсивный
for n in range(3220, 14,-1):
    if n >= 3210: f[n] = 1 #нерекурсивный 
    else: f[n] = f[n+3]+7 #рекурсивный
print(f[15]-g[3000])

from functools import*
@lru_cache(None) #сохраняем в оперативку значения функций
def f(n):
    if n >= 3210: return 1
    else: return f(n+3)+7
@lru_cache(None)
def g(n):
    if n < 10: return n
    else: return g(n-3)+5
for n in range(-10, 2800): g(n)
for n in range(3000, 20,-1): f(n)
print(f(15) - g(3000))
    
    
from functools import lru_cache
@lru_cache(None)
def f(n):
    if n <= 1:
        return 1
    return f(n - 1) - f(n - 2) + 5
for i in range(1, 1050):
  f(i) #??????????
print(f(1040) - f(1015))
