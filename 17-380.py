op=open('17-380.txt')
x=list(int(s) for s in op)
m=0
summa=0
k=0
r=0
p=0
def dlina(a,b,c):
        r=0
        if len(str(abs(a)))==4: r+=1
        if len(str(abs(b)))==4: r+=1
        if len(str(abs(c)))==4: r+=1
        return r
for i in x: 
    if i%100==25:
        m=max(i,m)
print(m)
for i in range(len(x)-2):
    a=x[i]
    b=x[i+1] 
    c=x[i+2]
    if dlina(a,b,c)<=2:
        summa = a + b + c
        if summa <= m: 
            k+=1
            p=max(summa,p)
print('amount =',k,'sum =',p)

    

