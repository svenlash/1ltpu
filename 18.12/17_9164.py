f=open('17_9164.txt')
a=[int(i) for i in f]
m=max(i for i in a if i%17==0)
k=0
mx=0
for i in range (len(a)-1):
    b=a[i:i+2]
    if sum(b)>m:
        k+=1
        mx=max(sum(b),mx)
print(k,mx) #5104 19930N
