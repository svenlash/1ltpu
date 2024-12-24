f=open('172.txt')
a=[int(i) for i in f]
m=max(i for i in a if i%401==0)
def f(x):
    return sum(int(i) for i in str(x))
k=0
mn=10**8
for i in range(len(a)-2):
    b=a[i:i+3]
    if ((f(b[0])!=f(b[1])
         and f(b[0])!=f(b[2])
         and f(b[1])!=f(b[2]))
        and (sum(b)>m)): #нельзя все условия сразу
        k+=1
        mn=min(mn, sum(b))
print(k,mn) #6283 9627
