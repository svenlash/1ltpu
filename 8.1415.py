from itertools import product 
a=list(product('12345', repeat=8))
#sp=[x for x in a if (x.count('4')==1 and x.count('5')==1) or (x.count('4')==2 and x.count('5')==0) or (x.count('5')==2 and x.count('4')==0)]
#sp=[x for x in a if x.count('4')==2]
otw=0
for i in a:
    i=str(i)
    i=i.replace('5','4')
    if i.count('4')==2:
        otw+=1
print(otw)
