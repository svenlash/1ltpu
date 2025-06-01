time=[0]*24*60
a=open('26-6792.txt').readlines()
for k in a:
    l = k.split()
    for i in range(int(l[0]),int(l[1])+1):
            time[i]+=1
pick=[]
for i in range(len(time)):
    if time[i]==max(time):
        pick.append(i)
res=[]
for i in range(len(pick)-1):
    res.append(pick[i+1]-pick[i])
