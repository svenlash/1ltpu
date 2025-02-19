#как решать 5 задание 
#для начала как переводить системы счисления 
def tri(x): #перевод из 10 в 3 систему 
    s=''
    while x!=0:
        s=str(x%3)+s
        x//=3
    return(s)
print(tri(256)) #100111
#18119
a=[]
for n in range(1,1000):
    n1=tri(n)
    if sum(int(t) for t in n1)%2==0:
        n1='1'+n1+'2'
    else: n1='2'+n1+'0'
    r=int(n1,3)
    if r>100:
        a.append(r)
print(min(a)) #113

#16252
mn=10**9
for n in range(1,1000):
    n1=tri(n)
    if n%2==0:
        n1='2'+n1+tri(int(n1[-1])*2)
    else: n1 = tri(int(n1[0])*2)+n1+'2'
    r=int(n1,3)
    if r>100:
        mn=min(mn,r)
print(mn) #131



def t(x):
    s=''
    while x!=0:
        s=str(x%3)+s
        x//=3
    return s
res=[]
for n in range(1,100000):
    a=t(n)
    if n%3==0:
        a+=a[:2]
    else:
        c=t(n%3 * 5)
        a+=c
    r=int(a,3)
    if r>64:
        res.append(r)
print(min(res)) #68


def tri(x):
    s=''
    while x!=0:
        s=str(x%3)+s
        x//=3
    return s
mn=10**10
for n in range(1,10000):
    N=tri(n)
    if sum(int(i) for i in N)%4==0:
        N='1'+(N)[:-2]
    else:
        a=sum(int(i) for i in N)%4 * 3
        a1=tri(a)
        N=N+a1
    r=int(N,3)
    if r>353:
        mn=min(mn,r)
print(mn) #354



def q(x):
    i=''
    while x:
        i=str(x%4)+i
        x//=4
    return i
otv=[]
for n in range(1,100000,2):
    n1=q(n)
    if n%3==0:
        n1=n1[-1]+n1[1:-1]+n1[0]+'1'
    else:
        n1=n1+str(n%3)
    r=int(n1,4)
    if r<=340:
        otv+=[r]
print(max(otv)) #334
