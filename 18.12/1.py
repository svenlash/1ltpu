f=open('17.txt')
a=[int(i) for i in f]
m=max(i for i in a if i%1000==121)
k=0
mx=-10**9
for i in range(len(a)-2):
    b=a[i:i+3] #i по i2
    q=[len(str(abs(k))) == 4 and abs(k)%2==0 for k in b] #потом складываем количество единиц 
    if sum(q)<=1 and sum(b)<=m:
        k+=1
        mx=max(mx,sum(b))
print(k,mx) #5211 20116
