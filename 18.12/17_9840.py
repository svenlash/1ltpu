f=open('17_9840.txt')
a=[int(i) for i in f]
m=max(i for i in a if len(str(abs(i)))==4 and abs(i)%100==39)
k=0; mx=0
for i in range(len(a)-1):
    b=a[i:i+2]
    q= (len(str(abs(b[0])))==4) + (len(str(abs(b[1])))==4)
    if q==1:
        if sum(b)**2 <= m**2:
            k+=1
            mx=max(mx,sum(b))
print(k,mx) #1591 9233
