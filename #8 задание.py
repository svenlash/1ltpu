from itertools import*
mx=-1000
k=0
#19240 - 6406 ЬЯРЯР 
'''for x in product(sorted('ЯНВАРЬ'), repeat=5):
    x=''.join(x)
    k+=1
    if x[0] not in 'Я' and 'ЯЯ' not in x and x.count('Ь')<=1:
        mx=max(k,mx)
    if k==mx: 
        n=x
print(mx, n)'''
#17671 - 274 ЙАЙАЙ
'''for x in map(''.join, product('АЙЛМ', repeat=5)):
    k+=1
    if 'М' not in x and 'Л' not in x and 'ЙЙ' not in x:
        mx=max(mx,k)
    if k==mx: print(mx, x)'''
#17627 - 86375
'''for x in product('0123456789SSSSS',repeat=5):
    x=''.join(x)
    if x.count('8')==1 and x.count('S')>=2:
        k+=1
print(k)'''
#17549 - 2313
'''for s in product(sorted('ФОКУС'),repeat=5):
    s=''.join(s); k+=1
    if s.count('Ф')==0 and s.count('У')==2: K=k
print(K)'''
#17521 - 9135
'''for a in product('01234567',repeat=5):
    a=''.join(a)
    if a[0] not in '01357' and a[-1] not in '26' and a.count('7')<=2:
        k+=1
print(k)'''
#15320 - 131
'''for i in map(''.join, product('АПРСУ', repeat=5)):
    k+=1
    if i.count('У')<=1 and 'АА' not in i: 
        print(k)    
        break'''
#9831 - 6720
cnt=0
for a in permutations('0123456789ABCDEF', 3): 
    for i in range(len(a)-1):
        b=a[i:i+2]
        if (int(b[0], 16)%2==0 and int(b[1], 16)%2==0) or (int(b[0], 16)%2==1 and int(b[1], 16)%2==1): 
            k+=1
        if k==0: cnt+=1
print(cnt)

from itertools import *
k=0
for i in product('01', repeat=8):
    i=''.join(i)
    if i[0]=='1' and int(i)%4==0:
        k+=1
        print(i)
print(k) 
