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