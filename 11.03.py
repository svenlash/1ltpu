def f(n):
    if n%2==0 or n<=1: return n==2
    for i in range(3, (int(n*0.5)+1), 2):
        if n%i==0: return False
    return True
op=open('11.03.txt')
a=list(int(x) for x in op)
s=0
b=0
c=1e9
for i in range (len(a)-2):
    if '3' in str(a[i]) and '3' in str(a[i+1]) and '3' in str(a[i+2]):
        b=a[i]+a[i+1]+a[i+2]
        if f(b):
            s+=1
            c=min(c,b)
print(s)
print(c)

