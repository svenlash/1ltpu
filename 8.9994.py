from itertools import product
a=0
b=product('АКЛОШ', repeat=5)
for i in b:
    a+=1
    i=''.join(i)
    if i=='ШАЛАШ':
        print(a)