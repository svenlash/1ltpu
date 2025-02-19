mx=-10000
for n in range(4, 1000):
    s='2' + n * '5'
    while '222' in s or '555' in s:
        if '555' in s:
            s=s.replace('555', '2', 1)
        else:
            s=s.replace('222', '5', 1)
    x=[int(i) for i in s]
    mx=max(mx, sum(x))
print(mx)

from random import *
mnoj=set()
a=['3']*10 + ['7']*10 + ['5']*10
for i in range (1,1000):
    shuffle(a)
    s='>' + ''.join(a)
    while '>3' in s or '>5' in s or '>7' in s:
        if '>3' in s:
            s=s.replace('>3', '55>', 1)
        if '>5' in s:
            s=s.replace('>5', '5>3', 1)
        if '>7' in s:
            s=s.replace('>7', '3>5', 1)
    x=s[:-1]
    summa= sum ([int(i) for i in x])
    mnoj.add(summa)
print(summa, mnoj) #на каждой итерации одно значение т.к. шафл

   
            
