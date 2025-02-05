k=0
r=0
from itertools import * 
for i in product(sorted('ДОКЛА'),repeat=5):
  i=''.join(i)
  k+=1
  if i=='ЛОДКА': k1=k
  if i=='ОКЛАД': k2=k
  if k>=2411 and k<=2827: 
    if i[2]=='Д' and i.count('О')==2 and i[-2] in 'ДКЛ':
      r+=1
  #2 способ 
  if 'ЛОДКА' <= i <= 'ДОКЛА' and i[2]=='Д' and i.count('О')==2 and i[-2] in 'ДКЛ':
    r+=1
print(r)

k=0
from itertools import * 
for x in permutations(sorted('СВОБДА'),5):
  x=''.join(x)
  if 'ОСОБА' < x < 'СДОБА' and len(x)==len(set(x)): #проверка на повтор
    k+=1
print(k)

k=0
from re import *
from itertools import *
for s in product('0123456789AB', repeat = 5):
  if s[0]!='0': s=''.join(s)
  if s.count('7')==1 and s.count(r'[9AB]')<=3:
    k+=1
print(k)

k=0
from itertools import *
for s in permutations('012346789',5):
  s=''.join(s)
  if s[0]=='0':
    continue
  for l in s:
    if int(l)%2==0: 
      s=s.replace(l, '*')
    else: 
      s=s.replace(l, '!')


























  if '**' not in s and '!!' not in s: 
    k+=1
print(k)
