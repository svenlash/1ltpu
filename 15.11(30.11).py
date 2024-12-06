def s(x,y,c):
    return x*y>c
def f(x,y,c):
    return (s(x,y,c+13)==0)<= (s(28, y, 520) or s(x,25,800))
for c in range(-100,999):
    if all(f(x,y,c) for x in range(1,100) for y in range(1,100)):
        print(c)
# -13