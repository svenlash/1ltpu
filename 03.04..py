#a='Какой ваш любимый учитель?\n1-Cудакова\n2-Ромашова\n3-Архипова
#print(a)
#tch=int(input('Введите число = '))
##while tch = int(input('Введите число = '))) in [1,2,3]:
import re
x=True
while x :
    v=r'{A-Za-z}'
    print(v)
    a='Какой ваш любимый учитель?\n1-Cудакова\n2-Ромашова\n3-Архипова'
    print(a)
    tch=(input('Введите число = '))
    b=' Предмет:'
    if tch in '123':
        match int(tch):
            case 1:
                print(b+' Русский язык')
            case 2:
                print(b+' Математика')
            case 3:
                print(b+' Химия')
    elif tch in v:
        print('Ошибка')
        x=False 

