#ПЛОХОЙ СПОСОБ ТРЕБУЕТ ЗАКРЫТИЯ ФАЙЛА
summa=0
otkrit=open("26.02.txt")
list=otkrit.readlines()
for s in list:
    summa += int(s)
otkrit.close()
print(summa)
