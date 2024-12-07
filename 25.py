'''def f(x):
    a = set()
    for i in range(2,int(x**0.5) +1):
        if x % i==0:
            a.add(i)
            a.add(x//i)
    return sorted(a)

cnt = 0
for x in range(123456, 10**10):
    if cnt == 5:
        break
    a = f(x)
    if len(a)==4:
        cnt+=1
        print(x,sum(a))'''

# МАСКИ
from fnmatch import *
# 1
'''
for x in range(96437,10**10, 96437):
    if fnmatch(str(x), '7?2*4??9?') and x % 96437 == 0:
        print(x, x//96437)'''
# 2
'''
for x in range(124, 10**9,124):
    if fnmatch(str(x), '1?3**5?') and not(fnmatch(str(x), '1*77*1')) and not(fnmatch(str(x), '7*11*7')):
        print(x, x//124)'''


# в fnmatch также есть
# [123...] - одно из представленных
# [!123...] - НЕ одно из представленных

# 3
'''
for x in range(11071,10**10,11071):
    if fnmatch(str(x), '[123579]136*[02468]1') or fnmatch(str(x),'[123579]136'):
        print(x,x//11071)
'''

# 4
'''
def f(x):
    a = set()
    for i in range(2,int(x**0.5) +1):
        if x % i==0:
            a.add(i)
            a.add(x//i)
    return sorted(a)
print(f(16))
for x in range(1,10**6):
    b = [i for i in f(x) if fnmatch(str(i), '4*')]
    if len(b) == 24:
        print(x, max(b))'''

# 17880
'''for x in range(1917,10**10,1917):
    if fnmatch(str(x), '3?12?14*5'):
        print(x, x//1917)'''

# 7357
'''for x in range(53191,10**10,53191):
    if fnmatch(str(x), '[02468]136*[13579]') or fnmatch(str(x), '[02468]136'):
        print(x,x//53191)
'''

# 7724
'''
def f(x):
    a = set()
    for i in range(2,int(x**0.5) +1):
        if x % i==0:
            a.add(i)
            a.add(x//i)
    return sorted(a)

for x in range(1018, 10**9,1018):
    if fnmatch(str(x), '*18??18') and x % 18 ==0:
        print(x, len(f(x))+2)'''

# 8960
'''
def f(x):
    a = set()
    a.add(1)
    a.add(x)
    for i in range(2,int(x**0.5) +1):
        if x % i==0:
            a.add(i)
            a.add(x//i)
    return sorted(a)
for x in range(500000, 10**100):
    if fnmatch(str(sum(f(x))), '*7?'):
        print(x, sum(f(x)))
'''

# 13832
'''
for x in range(7777,10**9,7777):
    if fnmatch(str(x), '[02468][13579][02468][02468][13579][02468][13579]77'):
        print(x,x//7777)'''

# 14440
'''
def num_mul(x):
    result = 1
    for i in str(x):
        result*=int(i)
    return result

def f(x):
    a = set()
    a.add(1)
    a.add(x)
    for i in range(2,int(x**0.5) +1):
        if x % i==0:
            a.add(i)
            a.add(x//i)
    return sorted(a)

for x in range(1,10**7):
    if fnmatch(str(x), '31*567?') and len(f(x)) == 2:
        print(x, num_mul(x))'''

# 11251
'''for x in range(2291,10**10,2291):
    if fnmatch(str(x), '*222132?'):
        print(x, x//2291)'''

































































