#abs(absolut) - модуль
op=open('17-381.txt')
m=0
x=[int(s) for s in op]
for i in x:
    if i%100==39 and len(str(abs(i)))==4:
        m=max(i,m) #(i,m - сравнивает)
print(m)