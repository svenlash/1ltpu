from turtle import *
up()
tracer(0,0)
k=10
screensize(3000,3000)
for x in range(-50,50):
    for y in range(-50,50):
        goto(k*x, k*y)
        dot(3)
home()
down()
left(90)
right(60)
for _ in range(2):
    fd(k*7)
    rt(120)
rt(300)
fd(k*7)
for __ in range(2):
    rt(60)
    fd(7*k)
    rt(60)
done()
