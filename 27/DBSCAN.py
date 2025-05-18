https://education.yandex.ru/ege/task/2e3573f2-3e95-4773-a660-592288a1c946
# Доступны файлы для чтения: 27_А.txt, 27_А.xlsx, 27_B.txt, 27_B.xlsx
#A код 
from math import * 
f=open('27_А.txt')
a=[list(map(float,i.replace(',','.').split())) for i in f]
cl=[]
while a: 
  cl.append([a.pop(0)])
  for j in cl[-1]: 
    for i in a[:]: 
      if dist(j,i)<=5: 
        cl[-1].append(i)
        a.remove(i)
cl=[i for i in cl if len(i)>=100]


def f(cl): 
  xc,yc,mn=0,0,10**10
  for j in cl:
    sumd=sum(dist(j,i) for i in cl)
    if sumd<mn: 
      mn=sumd
      xc=j[0]
      yc=j[1]
  return xc,yc
result=[f(k) for k in cl]
Px=sum(p[0] for p in result)/len(result)
Py=sum(p[1] for p in result)/len(result)
print(int(Px*10000), int(Py*10000))

#B код
from math import * 
f=open('27_B.txt')
a=[list(map(float, i.replace(',','.').split())) for i in f]
cl=[]
while a: 
  cl.append([a.pop()])
  for j in cl[-1]: 
    for i in a[:]: 
      if sit(j,i)<=5: 
        cl[-1].append(i)
        a.remove(i)
cl=[i for i in cl if len(i)>=100]
def f(cl): 
  xc,yc,mn=0,0,10**10 
  for j in cl: 
    sumd=sum(dist(j,i) for i in cl)
    if sumd<mn: 
      mn=sumd
      xc=j[0]
      yc=j[1]
  return xc,yc
result=[f(k) for k in cl]
Px=sum(p[0] for p in result)/len(result)
Py=sum(p[1] for p in result)/len(result)
print(int(Px*10000), int(Py*10000))
    
  

