a=int(input('Введите номер месяца: '))
x='Время года:'
if a>=1 and a<=12:
    if a>=3 and a<=5:
        print(x,'Весна')
    if a>=6 and a<=8:
        print(x,'Лето')
    if a>=9 and a<=11:
        print(x,'Осень')
    else:
        print(x,'Зима')
else:
    print('Такого месяца нету((')
