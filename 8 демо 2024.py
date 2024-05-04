from itertools import permutations
a=permutations('01234567', 5)
sp=[x for x in a if x.count('1')==0 and x[0]!='0' and len(set(x))==len(x)]
#set !!!
summa=0
for i in sp:
    flag=1
    for x in range(len(i)-1):
        if int(i[x])%2 == int(i[x+1])%2:
            flag = 0 
    if flag == 1: 
        summa+=1
print(summa)