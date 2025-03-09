'''from itertools import *
k=0
for i in product('CNCNCNC', repeat=5):
    i=''.join(i)
    if 'CCC' not in i:
        if i.count('CC')>=2:
            k+=1
print(k)'''
from turtle import *
up()
tracer(0)
k=20
screensize(3000,3000)
for x in range(-50,50):
    for y in range(-50,50):
        goto(k*x, k*y)
        dot(3)
home()
left(90)

down()
for w in range(2):
    fd(23*k)
    lt(90)
    back(27*k)
    lt(90)
up()
back(5*k)
rt(90)
fd(11*k)
lt(90)
down()
for k in range(2):
    fd(26*k)
    rt(90)
    fd(32*k)
    rt(90)
done()