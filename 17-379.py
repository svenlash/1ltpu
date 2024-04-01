op=open('17-379.txt')
x=list(int(s) for s in op)
nn=0
c=0
m=0
#range - диапазон
for i in x:
    if i%100==15:
        m=max(i, m)
cc=0
for i in range(len(x)-2):
    summ = x[i] + x[i+1] + x[i+2]
    if (len(str(x[i]))==4 and len(str(x[i+1]))!=4 and len(str(x[i+2]))!=4) \
       or (len(str(x[i]))!=4 and len(str(x[i+1]))==4 and len(str(x[i+2]))!=4)\
       or (len(str(x[i]))!=4 and len(str(x[i+1]))!=4 and len(str(x[i+2]))==4) and  summ >= m:
        c+=1
        cc=max(summ,cc)
print(c, cc)   
