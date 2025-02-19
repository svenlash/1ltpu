from turtle import *
tracer(0)
screensize(3000,3000)
k=15
pensize(15)
color('black')
fillcolor('green')
begin_fill()
for _ in range(9):
    fd(22*k)
    rt(90)
    fd(6*k)
    rt(90)
up()
fd(1*k)
rt(90)
fd(5*k)
lt(90)
down()
end_fill()
for __ in range(9):
    fd(53*k)
    rt(90)
    fd(75*k)
    rt(90)
up()
for x in range(-50,50):
    for y in range(-50, 100):
        goto(x*k, y*k)
        dot(4, 'red')
down()
done()
