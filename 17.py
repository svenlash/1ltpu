a=open('17.txt')
x=max([int(i) for i in a if len(str(abs(int(i))))==3]) ** 3
r=[int(i) for i in a]
k=0
mx=-10**8
for i in range (len(r)-1):
    b=a[i:i+2]
    bb=[int(i) for i in str(abs(b[0]))]
    bbb=[int(i) for i in str(abs(b[1]))]
    if (sum(bb) % 5 == 0 and sum(bbb) % 5 != 0) or (sum(bb) % 5 != 0 and sum(bbb) % 5 == 0):
        if abs(b[1] ** 2 - b[0] ** 2) >= x:
            k+=1
            mx = max ( b[0] + b[1], mx) 
print(k, mx) 

a=open('17_17097.txt')
x=int(i for i in a)
mn=min([int(i) for i in a if i%100==17])
print(mn)
