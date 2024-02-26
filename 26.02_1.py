#ПЛОХОЙ СПОСОБ ТРЕБУЕТ ЗАКРЫТИЯ ФАЙЛА
otkrit = open("26.02.txt")
summa = 0
while True:
    s = otkrit.readline()
    if not s: break
    summa+=int(s)
otkrit.close()
print(summa)