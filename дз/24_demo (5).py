''' 
27421
a=open('24_demo (5).txt').read()
k=1
mx=-10**3
for i in range (len(a)-1):
    if a[i]!=a[i+1]:
        k+=1
    else: mx=max(mx, k); k=1
print(mx)'''

'''
27686
x=open('24__.txt').read()
x=x.replace('Y',' ')
x=x.replace('Z',' ')
s=x.split(' ')
mx=-10000
for i in s:
    mx=max(mx, len(i))
print(mx)'''

#!!!!!!!!
'''
27689
f=open('244.txt').read()
k=0
mx=-10000
for i in range(len(f)):
    if f[i]=='X' and k%3==0 or f[i]=='Y' and k%3==1 or f[i]=='Z' and k%3==2:
        k+=1
    elif f[i]=='X': k=1
    else: mx=max(mx, k); k=0
print(mx)'''

'''27694
a=open('2244.txt').read()
mx=-10000
k=0
for i in range(len(a)):
    if a[i]=='A' and k%2==0 or a[i]=='B' and k%2==1:
        k+=1
    elif a[i]=='A': k=1
    else: mx=max(mx, k); k=0
print(mx)'''

#29672
'''a=open('29672.txt').readlines()
k=0
#считаем количество строк по условию 
for i in a:
    if i.count('E') > i.count('A'):
        k+=1
print(k)
#альт решение
f = open('24.txt')
c = 0
i = f.readline()
while i != '':
    if i.count('E') > i.count('A'): c += 1
    i = f.readline()
print(c)'''

#33196
'''
a=open('33196.txt').read()
alf='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
i=[0]*26
a=a.split('A')
#правильнее писать так: a=a[a.find('A'):].split('A')
for k in a:
    if k!='':
        i[alf.index(k[0])]+=1 #сколько раз встречается каждая буква 
print(alf[i.index(max(i))]) #наиболее частная '''
#33526
'''a=open('33526.txt').read()
alf='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
res=[]
mx=-100000
for i in range(len(a)-2):
    if a[i]==a[i+2]:
        res.append(a[i+1])
for i in set(res):
    mx=max(mx,res.count(i))
for i in set(res):
    if mx==res.count(i): print(i)
print(res, set(res))
'''

#35998
a=open('2424.txt').readlines()
mx=0
for i in a:
    if i.count('A') < 25:
        for k in set(i):
            mx=max(i.rfind(k)- i.find(k), mx)
            #rfind - первое вхождеине справа 
print(mx)




































































