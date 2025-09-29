a=open('171.txt')
x=[int(i) for i in a]
mn=min(x)
k=0
mx=-10**6
for i in range(len(x)-1): 
    b=x[i:i+2]
    if b[1]%43==mn and b[1]%43==mn:
        k+=1
        b1=int(b[1])
        b0=int(b[0])
        mx=max(mx,max(b1,b0)-min(b1,b0))
print(k, mx)
