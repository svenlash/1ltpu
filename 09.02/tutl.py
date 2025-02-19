import turtle as t
#19922
k=15
t.up()
t.tracer(0,0)
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
    t.up()
#сетка 
t.home()
t.down()
for i1 in range(95):
        t.forward(12*k)
        t.right(120)
t.up()
t.goto(0,0)
t.right(210)
t.forward(5*k)
t.left(90)
t.down()
for i2 in range(95): #снизу то, что в скобочках
    t.forward(12*k)
    t.right(120)    
t.update()
t.done()
