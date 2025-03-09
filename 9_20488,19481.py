'''f=open('9_20488.txt')
k=0
for line in f:
    x = [int(i) for i in line.split()]
    q1 = [i for i in x if x.count(i)==1]
    q2 = [i for i in x if x.count(i)>1]
    if len(q1)>0 and len(q2)>0:
        if max(x) in q1:
            if sum(q1)/sum(q2) >= 3:
                k+=1
print(k)


x = open('9_19481.txt')
k=1
#считаем с первой !!!
res=[]
for l in x:
    a = [int(i) for i in l.split()]
    q =[i for i in a if a.count(i)==1]
    k+=1
    if a == q:
        q=sorted(q)
        if (q[0]+ q[3])**2 > q[1]**3 + q[2]**3:
            res+=[k]
print(sum(res))
f = open('9 1.txt')
k=0
r=[]
for l in f:
    k+=1
    x = [int(i) for i in l.split()]
    q2 = [i for i in x if x.count(i) == 2]
    q3 = [i for i in x if x.count(i) == 3]
    q1 = [i for i in x if x.count(i) == 1]
    if len(q2)==2 and len(q3)==3 and len(q1)==3:
        if q3[0]> q2[0]: r+=[k]
print(r)
k=0
f = open('9 2.txt')
for l in f:
    x=[int(i) for i in l.split()]
    q3 = [i for i in x if x.count(i)==3]
    q1 = [i for i in x if x.count(i)==1]
    q = [i for i in x if x.count(i)>1]
    if len(q3)==3 and len(q1)==3:
        if sum(q)**2 > sum(q1)**2:
            k+=1
print(k)

f = open('99.txt')
k=0
for l in f:
    k+=1
    x = [int(i) for i in l.split()]
    q1 = [i for i in x if x.count(i)==1]
    q3 = [i for i in x if x.count(i)==3]
    if len(q3)==6 and len(q1)==2:
        if min(x) in q1:
            print(k, sum(x))
            break

f = open('09.txt')
k=0
for l in f:
    x = [int(i) for i in l.split()]
    n = [i for i in x if i%2==1]
    c = [i for i in x if i%2==0]
    q2 = [i for i in x if x.count(i)==2]
    q1 = [i for i in x if x.count(i)==1]
    if len(c)>=0:
        s = sum(c)
    if len(c)==0:
        s = 0
    if ( (len(q2)==2 and len(q1)==3) and (sum(n) <= s) )  or ( (len(q2)!=2 and len(q1)!=3) and (sum(n) > s) ):
            k+=1
print(k)
'''

w = open('999.txt')
counter = 0
for p in w:
    y = [int(i) for i in p.split()]
    d2 = [j for j in y if y.count(j)==2]
    if len(d2)==6:
        if (d2[1]**2 +d2[3]**2 == d2[5]**2) or (d2[3]**2 +d2[5]**2 == d2[1]**2) or (d2[1]**2 +d2[5]**2 == d2[3]**2):
            counter += 1
print(counter)

