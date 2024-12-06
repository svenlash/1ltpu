
#sort изменяет функцию
#sorted возвращает отсортированный список 
# range 
# if i=0 
# continue 
# отсекает число 
#{} - множество
def f(x): #ФУНКЦИЯ НА ПОИСК ДЕЛИТЕЛЕЙ 
    a = set()
    for i in range (2, int(x**0.5)+1): #если только нетривиальные, то 1 меняем на 2
        if x%i==0:
            a.add(i)
            a.add(x//i)
    return(sorted(a))
print(f(750))
def is_simple(x): #ФУНКЦИЯ ПРОСТОЕ ЛИ ЧИСЛО
    for i in range(2, int(x**0.5)+1):
        if x%i==0:
            return False 
    return True
print((is_simple(13)))
#ДАЛЬШЕ ЗАДАНИЯ 
#1
for x in range(174457,174506):
    a = f(x)
    if len(a) == 2: 
        print(a)
#2
for x in range(114578,114617):
    a=f(x)
    b = [i for i in a if i%10==8]
    if len(b)>0:
        r=sum(b)
    else:
        r=0
    if r&10==6:
        (print(x,r))
#3
for x in range(25317, 51238):
    a=f(x)
    b =[i for i in a if is_simple(i)]
    if len(b)>=6:
        print(x,max(b))
#4
kubii=[i**3 for i in range(1,100,2)] #кубы различных натуральных нечетных 
def F(x): #ФУНКЦИЯ НА ПОИСК ДЕЛИТЕЛЕЙ 
    a = set()
    for i in range (2, int(x**0.5)+1): #если только нетривиальные, то 1 меняем на 2
        if x%i==0:
            a.add(i)
            a.add(x//i)
    a.add(x)
    return(sorted(a))
for x in range(228224,531136):
        a=F(x)
        b = [i for i in a if i in kubii]
        if len(b)>=4:
            print(len(b),max(b))
#5
def dell(x):
    a=set()
    for i in range(1,int(x**0.5)+1):
        if x%i==0:
            a.add(i)
            a.add(x//i)
    return(sorted(a))
for x in range(397438,443521):
    a=dell(x)
    k=[i for i in a if i%2==0]
    if len(k)>=142:
        print(len(k),max(k))