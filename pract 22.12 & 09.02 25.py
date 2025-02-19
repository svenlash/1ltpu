'''from fnmatch import * 
for i in range(10**8, 10**10 + 1 , 42): 
  if fnmatch(str(i), '48*15*0'):
    if i%42==0: 
      print(i, i//42)
'''
'''def f(x, y): 
  if x<y: return 0 
  if x==y: return 1 
  x1=sum([int(i) for i in str(x)])
  x2=int(str(x**2)[0])
  return f(x-x1, y) + f(x-x2, y)
print(f(32, 1))'''

'''for n in range(1,60): 
  a=bin(n)[2:]
  if n%2==0: 
    a= a + '0' * a.count('0')
  else:
    a = '1' * a.count('1') + a 
  r=int(a, 2)
  if r>2000: 
    print(n)'''

'''from fnmatch import * 
for i in range(42, 10**10 + 1, 42): 
  if fnmatch(str(i), '48*15*0'):
    if i%42==0: 
      print(i, i//42)
'''
'''a=open('24.txt').readline()
k=0
a=a.replace('ABA', 'A BA')
a=a.split()
print(a)
for i in range(len(a)-1): 
    if ('ABA' in a[0] or 'BAB' in a[i]) and ('ABA' in a[i+1] or 'BAB' in a[1]):
        k+=1
print(k)
'''
from functools import *
@lru_cache(None)
def f(n): 
  if n>=2024: return 1 
  else: return f(n+2) + f(n+4)
a=set()
for n in range(1028, 3000): 
  a.add(f(n))
print(len(a))


alf='0123456789ABCDE'
mx=10**10
for x in alf:
    m=int('432'+x+'3',15)
    n=int('86'+x+'86',15)
    for i in range(0,100):
        a=n*i-m
        if a>=1:
            mx=min(a,mx)
print(mx)

mn=10**10
for i in range(1000,10000):
    x=[]
    a=int(str(i)[0])
    b=int(str(i)[1])
    c=int(str(i)[2])
    d=int(str(i)[3])
    x.append(a*b)
    x.append(a*c)
    x.append(a*d)
    x=sorted(x)
    s=str(x[-2])+str(x[-1])
    if s=='5472':
        mn=min(i,mn)
print(mn) #9068 

for i in range(1000,10000):
    b=[int(x) for x in str(i) if int(x)%2==0]
    c=sum(b)**2
    cif=[int(x) for x in str(i)]
    sss=(max(cif)-min(cif))**3
    N=str(min(c,sss))+str(max(c,sss))
    if N == '4343':
        print(i)
        break #1027 

f=open('1777.txt')
def F(a):
    return (int(str(a[0]).count('0') == 0)+int(str(a[1]).count('0') == 0)+
            int(str(a[2]).count('0') == 0))>=2
        
a=[int(i) for i in f]
m=max(a)
k=0
mn=-10**8
for i in range(len(a)-2):
    b=a[i:i+3]
    if sum(b)<m/2 and F(b):
        k+=1
        mn=max(mn,sum(b))
print(k,mn)


alf='ВЬЮГА'
cnt=0
for i1 in alf:
    for i2 in alf:
        for i3 in alf:
            for i4 in alf:
                for i5 in alf:
                    for i6 in alf:
                        s=i1+i2+i3+i4+i5+i6
                        if 'ЮГ' in s:
                            cnt+=1
print(cnt) #2976 '''


alf='0123456789ABCD'
k=0
for i1 in alf[1:]:
    for i2 in alf:
        for i3 in alf:
            for i4 in alf:
                for i5 in alf:
                    s=i1+i2+i3+i4+i5
                    if s.count('9')==1 and (int(s.count('B'))+int(s.count('C'))+int(s.count('D')))<=3:
                        k+=1
print(k) #133612 


def pp(x):
    s=''
    while x:
        s=str(x%5)+s
        x//=5
    return s
def ss(x):
    s=''
    while x:
        s=str(x%7)+s
        x//=7
    return s
for x in range(1000000, 10000, -1):
    a=pp(x)
    b=ss(x)
    if a[-1]=='2' and b[-1]=='3':
        if len(a)<=6 and len(b)<=5:
            print(x, a, b)














































                        
