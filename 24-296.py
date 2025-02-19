a=open('24-296.txt')
a=a.readline()
a=a.replace('AF','1 0')
c=[x for x in a.split()]
k=0
for i in range(len(c)-200-1):
    s=0
    for x in range(i,i+200+1):
        s+=len(c[x])
    k=min(s,k)
print(s)
