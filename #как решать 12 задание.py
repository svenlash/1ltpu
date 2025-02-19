#как решать 12 задание 
#17866
''' 
s = '1' * 81 
while '11111' in s or '888' in s:
    if '11111' in s: 
        s=s.replace('11111', '88', 1)
    else: s=s.replace('888','8')
print(s) 
881'''
#19244
'''for  n in range (4, 10000):
    s='1' + n * '2'
    while '12' in s or '322' in s or '222' in s:    
        if '12' in s: 
            s=s.replace('12','2',1)
        if '322' in s: 
            s=s.replace('322','21',1)
        if '222' in s: 
            s=s.replace('222','3',1)
    r = sum(int(i) for i in s)
    #r = s.count('1') + s.count('2') + s.count('3')
    if r==15: print(n); break
    37'''
#19152
'''sq=[i**3 for i in range(1,100)]
for n in range(3,10000):
    s='59' +'8'*n
    while '68' in s or '988' in s or '888' in s:
        if '68' in s: s=s.replace('68', '8', 1)
        if '988' in s: s=s.replace('988', '86', 1)
        if '888' in s: s=s.replace('888', '9', 1)
    r=sum(int(i) for i in s)
    if r in sq:
        print(n); break
7 '''