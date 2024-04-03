while True:
    a='Какой ваш любимый учитель?\n1-Cудакова\n2-Ромашова\n3-Архипова'
    print(a)
    tch=int(input('Введите число = '))
    b=' Предмет:'
    if tch < 1 or tch > 3:
        print('Ошибка!')
        False  
    if tch<=3 and tch>=1:
        True
        match tch:
            case 1:
                print(b+' Русский язык') 
            case 2:
                print(b+' Математика') 
            case 3:
                print(b+' Химия')
                
                
            
        
