#17682
def f(x,y):
    if x>=67:
        return y%2==0 
    #проверяем кто победил 
    #Петя - первый, нечет 
    #Ваня - второй, чет 
    if y==0:
        #Осталось 0 ходов, значит никто не победил 
        return 0
    Hodi = [f(x+1,y-1), f(x+3, y-1), f(x*2, y-1)]
    #y-1 - убавляем количество ходов 
    return any(Hodi) if y%2==1 else all(Hodi)
    #тернальный оператор 
    #any - хоть одна истина, all - все истинны
print([s for s in range(1,67) if f(s, 2)])
print([s for s in range(1,67) if f(s, 3) and not f(s, 1)])
print([s for s in range(1,67) if f(s, 4) and not f(s, 2)])






#17532
def f(a, b, m):
    if a+b >=65: 
        return m%2==0
    if m==0:
        return 0 
    h =[f(a+1, b, m-1), f(a, b+1, m-1),
        f(a*3, b, m-1), f(a, b*3, m-1)]
    return any(h) if m%2==1 else all(h)
    #для 19 меняем all на any - т к неудачный первый ход
print(min([s for s in range(1,59) if f(6,s,2)])) 
print([s for s in range(1,59) if f(6,s,3) and not f(6, s, 1)])
print([s for s in range(1,59) if f(6,s,4) and not f(6, s, 2)])






def f(x, y):
    if x>=172:
        return y%2==0
    if y==0: return 0
    h = [f(x+1, y-1), f(x+2, y-1), f(x+3, y-1), f(x*2, y-1)]
    return any(h) if y%2==1 else all(h)
print([s for s in range(1, 172) if f(s, 2)])
    


def f(a, b, m):
    if a+b<=72:
        return m%2==0
    if m==0:
        return 0
    h = [f(a-3,b,m-1), f(a, b-3, m-1), f(a-a//2, b, m-1), f(a, b-b//2, m-1)]
    return any(h) if m%2==1 else all(h)
print(max([s for s in range(23,1000) if f(50, s, 2)])) #94
print([s for s in range(23,1000) if f(50, s, 3) and not f(50, s, 1)])
print([s for s in range(23,1000) if f(50, s, 4) and not f(50, s, 2)])
































