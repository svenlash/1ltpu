k=0
for a in range(-100,100):
    flag=True
    for x in range(-100,100):
        for y in range(-100,100):
            if (((a<x)or((x**2)-(7*x)+10)>0)and((a>=y)or((y**2)+(7*y)+12>0)))==0:
                flag=False
                break
    if flag:
        k+=1
print(k)
'''5'''
