#64891
import turtle as t
t.speed(4)
k=20
'''
t.up()
#t.tracer(0,0)

t.goto(-15*k, -15*k)
for x in range(-15,15):
    for y in range(-15,15):
        t.goto(x*k, y*k)
        #t.down()
        t.dot(3)
    t.up()
t.home()
for y in range(-15,15):
    for x in range(-15,15):
        t.goto(x*k, y*k)
        #t.down()
        t.dot(3)
    t.up()'''

t.home()
t.down()
for i in range(4):
    for ii in range(4):
        t.forward(6*k)
        t.right(90)
    t.forward(10*k)
    t.right(90)
    t.forward(3*k)
t.update()
t.done()
