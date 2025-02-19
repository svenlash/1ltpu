#70533
import turtle as t
k=12
t.up()
t.goto(-10*k, -10*k)
t.tracer(0,0)
for x in range(-40,40):
    for y in range(-40,40):
        t.goto(x*k, y*k)
        t.dot(3)
    t.up()
for y in range(-40,40):
    for x in range(-40,40):
        t.goto(x*k, y*k)
        t.dot(3)
    t.up()
t.home()
t.down()
for i in range(9):
    t.forward(22*k)
    t.right(90)
    t.forward(6*k)
    t.right(90)
t.up()
t.forward(k)
t.right(90)
t.forward(5*k)
t.left(90)
t.down()
for i2 in range(9):
    t.forward(53*k)
    t.right(90)
    t.forward(75*k)
    t.right(90)
t.update()
t.done()
